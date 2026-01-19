# eChem Marseille 2026

## Insatllation instructions using conda

We recommend installing the required software through conda using the provided [`echem-marseille.yml`]() file. For this, you will have to install conda first, if you don't already have it installed. We recommend using the minimal conda installer called [miniconda](https://www.anaconda.com/download/success). Follow the [instructions](https://docs.anaconda.com/miniconda/install/) for your operating system on the [miniconda website](https://docs.anaconda.com/miniconda/install/).


Once you have miniconda, you can install the required conda packages using a command prompt. For Linux and macOS, you can directly use a terminal. For Windows, we recommend using the **Anaconda Powershell prompt**, which should be available as soon as you have installed miniconda.

### Create the echem environment

Using the [`echem-marseille.yml`]() file provided, all needed packages can be installed using the terminal command.

```
conda env create -f echem-marseille.yml
```

Once the installation is finished, activate the new conda environment:

```
conda activate echem-marseille
```

 To see that the installation worked correctly, start a Jupyter notebook by running the command:

```
jupyter-lab
```

This command will start the notebook in your default browser. Create a new notebook with the Python3 ipykernel and run the following Python code in the first cell:

```
import veloxchem as vlx
```

If the cell runs and you get no errors, then the installation worked correctly. If you run into any issues, you are welcome to join an online video meeting with us on **Wednesday 13 May** at **13:00**, where we will help you with the installation and answer your questions. A link to the meeting will be sent to all registered participants.

### Troubleshooting for Windows users

If ipykernel crashes when running `import veloxchem`, the cause may be the use of an incorrect MPI library. You can check this, by running Python in the Anaconda Power Shell:

```
python
import veloxchem as vlx
```

If, when importing veloxchem, you get the error below, the issue is related to the MPI library:

```
Abort(1090959) on node 0 (rank 0 in comm 0): Fatal error in PMPI_Init_thread: Unknown error class, error stack:
MPIR_Init_thread(193)........:
MPID_Init(1715)..............:
MPIDI_OFI_mpi_init_hook(1594):
...
```

To fix this MPI issue, run the following command in the Anaconda Power Shell, with the echem-marseille conda environment active:


```
conda install msmpi -c conda-forge
```

For Windows users, the environment variable `KMP_DUPLICATE_LIB_OK` needs to be set to **TRUE**.
If you would like to set environment variables in the Anaconda Powershell prompt (instead of using os.environ in the notebook), use the following command: `$env:KMP_DUPLICATE_LIB_OK="TRUE"` (note that the Anaconda Powershell prompt is different from the Anaconda prompt).

### Removing a conda environment

In case, for any reasons, you may need to re-install the conda packages from scratch, you can remove a conda environment this way:

```
conda deactivate
conda env remove -n echem-marseille
```

After removing a conda environment, it's also good to clean the cache:

```
conda clean --all
```

