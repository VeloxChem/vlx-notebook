# SolvationFepDriver Case Studies

This directory contains practical case studies and tutorials demonstrating the capabilities of the `SolvationFepDriver`. API documentation and a general user manual are available at [veloxchem.org/docs/solvation/](https://veloxchem.org/docs/solvation/).

## Available Tutorials
1. **[Neutral Organic Solvation](1_Neutral_Solvation/tutorial_neutral_solvation.ipynb)**  
   An interactive Jupyter notebook demonstrating the automated workflow for computing hydration free energies using an on-the-fly generated GAFF force field. Suitable for local execution.
   
2. **[Protein-Ligand Binding (HPC Workflow)](2_Protein_Ligand_binding/README.md)**  
   A production-ready python execution script demonstrating how to evaluate absolute binding affinities in complex, non-homogeneous environments by processing existing OpenMM topologies. Designed for HPC cluster execution.

## Advanced Benchmarks & Reproducibility Data
The large-scale benchmark datasets and topology files discussed in the manuscript are permanently archived on Zenodo. 

You can access the full reproducibility packages here: **[https://zenodo.org/records/21290868](https://zenodo.org/records/21290868)**

The Zenodo archive includes:
* **High-Throughput Neutral Benchmarks (FreeSolv):** Execution scripts for 629 compounds.
* **Ionic Solvation (IonSolv):** Execution scripts and data extraction tools, including Galvani potential corrections.
* **Transition Metal Redox Potentials:** DFT-optimized coordinates and custom Lennard-Jones parameters for the $[\text{Ru(bpy)}_3]^{3+}/[\text{Ru(bpy)}_3]^{2+}$ redox couple.
* **Protein-Ligand Topologies:** The complete OpenMM `.pdb` and `.xml` files required to execute the T4 lysozyme case study.