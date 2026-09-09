# Case Study 2: Absolute Protein-Ligand Binding Affinity

This case study demonstrates how to compute the absolute binding free energy of a ligand (2-propylphenol) to a protein receptor (T4 lysozyme mutant). 

To close the thermodynamic cycle and evaluate the binding affinity ($\Delta G_{bind}$), we must perform two independent alchemical transformations:
1. **Bulk Reference:** Decoupling the ligand from bulk water.
2. **Complex Phase:** Decoupling the ligand from the fully solvated protein binding pocket.

The absolute binding free energy is then recovered as:
$$\Delta G_{bind} = \Delta G_{complex} - \Delta G_{water}$$

> **Note on Computational Resources**  
> Due to the system size of the solvated protein complex (>60,000 atoms), this specific calculation is intended for high-performance GPU nodes rather than local execution. Therefore, this tutorial is provided as a production-ready Python execution script designed to be submitted to an HPC cluster.
> 
> *The required OpenMM `.pdb` and `.xml` input files for this specific system are available in our [Zenodo repository](https://zenodo.org/records/21290868).*

## Workflow Files
* `run_fep.py`: The Python execution script demonstrating the `compute_solvation_from_openmm_files` API.