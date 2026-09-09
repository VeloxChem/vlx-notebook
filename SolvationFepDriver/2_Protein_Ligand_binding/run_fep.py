"""
run_fep.py
Execution script for absolute protein-ligand binding free energy.
Calculates both bulk water and complex phase decoupling in triplicates.
Designed for GPU-accelerated HPC nodes (HIP platform).
"""
import json
import math
import statistics
import veloxchem as vlx

def calculate_total_uncertainty(deltaf_dict):
    """Propagates error from the 4 FEP stages (sqrt of sum of variances)."""
    variance_sum = sum(deltaf_dict[f"Stage {i}"]['Uncertainty']**2 for i in range(1, 5))
    return math.sqrt(variance_sum)

def main():
    compound = 'JZ4'
    output_path = f'{compound}_binding_affinity_results.json'
    
    # Dictionary to store all detailed results and summaries for JSON export
    results_data = {
        "compound": compound,
        "runs": [],
        "summary": {}
    }  
    
    water_values = []
    complex_values = []
    binding_values = []
    
    print(f"=== Starting Protein-Ligand Binding Affinity Workflow for {compound} ===")

    for run_idx in [1, 2, 3]:
        print(f"\n--- Starting FEP Run {run_idx} ---")
        
        run_results = {"run_index": run_idx}
        
        # ---------------------------------------------------------
        # STEP 1: Bulk Water Phase
        # ---------------------------------------------------------
        print("1. Bulk Water Decoupling...")
        solv_water = vlx.SolvationFepDriver()
        solv_water.num_steps = 1500000
        solv_water.num_snapshots = 1000  
        solv_water.platform = 'HIP'
        solv_water.lambdas_stage1 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        
        ligand = vlx.Molecule.read_pdb('ligand.pdb')
        deltaf_water = solv_water.compute(ligand)
        
        fe_water = deltaf_water['free_energy']
        err_water = calculate_total_uncertainty(deltaf_water)
        water_values.append(fe_water)
        
        run_results["water_phase"] = deltaf_water
        run_results["water_phase"]["total_uncertainty"] = err_water
        print(f"   Water phase complete. Result: {fe_water:.2f} ± {err_water:.2f} kJ/mol")

        # ---------------------------------------------------------
        # STEP 2: Complex Phase
        # ---------------------------------------------------------
        print("2. Complex-Phase Decoupling...")
        solv_complex = vlx.SolvationFepDriver()
        solv_complex.num_steps = 1500000
        solv_complex.num_snapshots = 1000  
        solv_complex.platform = 'HIP'
        solv_complex.resname = compound
        solv_complex.lambdas_stage1 = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        
        deltaf_complex = solv_complex.compute_solvation_from_openmm_files(
            solute_pdb='ligand.pdb', 
            solute_xml='ligand.xml',
            system_pdb='system_equilibrated.pdb',  
            other_xml_files=['cspce.xml', 'amber14-all.xml'] 
        )
        
        fe_complex = deltaf_complex['free_energy']
        err_complex = calculate_total_uncertainty(deltaf_complex)
        complex_values.append(fe_complex)
        
        run_results["complex_phase"] = deltaf_complex
        run_results["complex_phase"]["total_uncertainty"] = err_complex
        print(f"   Complex phase complete. Result: {fe_complex:.2f} ± {err_complex:.2f} kJ/mol")
        
        # ---------------------------------------------------------
        # STEP 3: Store Intermediate Binding Affinity
        # ---------------------------------------------------------
        fe_bind = fe_complex - fe_water
        err_bind = math.sqrt(err_water**2 + err_complex**2)
        binding_values.append(fe_bind)
        
        run_results["binding_affinity_kJmol"] = fe_bind
        run_results["binding_affinity_uncertainty_kJmol"] = err_bind
        results_data["runs"].append(run_results)
        
        print(f"   -> Run {run_idx} Binding Affinity: {fe_bind:.2f} ± {err_bind:.2f} kJ/mol")
        
        # Save progressively
        with open(output_path, "w") as f:
            json.dump(results_data, f, indent=4)

    # ---------------------------------------------------------
    # Final Averaging and Standard Deviations
    # ---------------------------------------------------------
    avg_water = statistics.mean(water_values)
    std_water = statistics.stdev(water_values) if len(water_values) > 1 else 0.0
    
    avg_complex = statistics.mean(complex_values)
    std_complex = statistics.stdev(complex_values) if len(complex_values) > 1 else 0.0
    
    avg_bind = statistics.mean(binding_values)
    std_bind = statistics.stdev(binding_values) if len(binding_values) > 1 else 0.0
    
    results_data["summary"] = {
        "avg_water_kJmol": avg_water,
        "std_water_kJmol": std_water,
        "avg_complex_kJmol": avg_complex,
        "std_complex_kJmol": std_complex,
        "avg_binding_affinity_kJmol": avg_bind,
        "std_binding_affinity_kJmol": std_bind
    }
    
    # Final save with the appended summary
    with open(output_path, "w") as f:
        json.dump(results_data, f, indent=4)
    
    print(f"\n=== All FEP tasks complete for {compound} ===")
    print(f"Average Water Phase:   {avg_water:.2f} ± {std_water:.2f} kJ/mol")
    print(f"Average Complex Phase: {avg_complex:.2f} ± {std_complex:.2f} kJ/mol")
    print(f"Final Average Binding: {avg_bind:.2f} ± {std_bind:.2f} kJ/mol")
    print(f"Results successfully saved to {output_path}")

if __name__ == "__main__":
    main()