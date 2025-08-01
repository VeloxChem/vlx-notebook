# VeloxChem quantum-classical interoperability workflows

This folder contains Jupyter notebooks for VeloxChem connected to the article *VeloxChem quantum--classical interoperability for modeling of complex molecular systems*. To run the notebooks, you will need to install [VeloxChem](https://veloxchem.org/docs/intro.html) alongside a few other Python packages and our recommendation is to perform the installation using conda, as described below.

## Install miniconda

Download the appropriate installer for your operating system and follow the installation instructions on the [miniconda website](https://www.anaconda.com/docs/getting-started/miniconda/main).

## Create the conda environment

Using the `workflow.yml` file, you can create a conda environment called `workflow` and install all the needed packages to run the Jupyter notebooks in this repository.

```
conda env create -f workflow.yml
```

## Use the new environment

```
conda activate workflow
jupyter-lab Build.ipynb
```
