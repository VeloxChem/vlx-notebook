# Hessian code prototyping

This folder contains a notebook connected to the article [*eChem: Accelerated Method Development in Quantum Chemistry with Notebooks*](https://chemistry-europe.onlinelibrary.wiley.com/doi/10.1002/cmtd.202500033).

The notebook is also available as a Google Colab notebook that does not require installation of any packages on a local computer. The Google Colab notebook can be accessed here: [hessian_code_prototyping](https://colab.research.google.com/drive/1J97FYeWDwT_1bfkgt2cy58Sxof6S0lBU?usp=sharing). For those who would like to run the notebook locally, we provide two installation options: (1) using conda and (2) from source. Our recommendation is to install the required packages using conda, since it is more straightforward and available for all operating systems (Linux, Windows, and macOS), but installation from source is also possible for Linux and macOS users.

## (1) Installation using conda

We recommend installing the required software through conda using the provided `echem_hessian.yml` file. For this, you will have to install conda first, if you don't already have it installed. We recommend using the minimal conda installer called [miniconda](https://www.anaconda.com/download/success) (scroll down to the bottom of the page to find the Miniconda installers). Follow the [instructions](https://docs.anaconda.com/miniconda/install/) for your operating system on the [miniconda website](https://docs.anaconda.com/miniconda/install/).

Once you have miniconda, you can install the required conda packages using a command prompt. For Linux and macOS, you can directly use a terminal. For Windows, we recommend using the **Anaconda Powershell prompt**, which should be available as soon as you have installed miniconda.

### Create the echem-hessian environment

Using the `echem_hessian.yml` file provided, all needed packages can be installed using the terminal command.

```
conda env create -f echem_hessian.yml
```

Once the installation is finished, activate the new conda environment:

```
conda activate echem-hessian
```

You are ready to run the Jupyter notebook:

```
jupyter-lab hessian_code_prototyping.ipynb
```

This command will start the notebook in your default browser and you should be able to run it. Jupyter can access the folders below where it is spawned. Examples on how to use Jupyter can be found [here](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/examples_index.html).

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

To fix this MPI issue, run the following command in the Anaconda Power Shell, with the echem conda environment active:


```
conda install msmpi -c conda-forge
```

If the above fix does not work, we recommend that one remove the conda environment and install the packages manually (see Sections **Removing a conda environment** and **Manual installation** below). 

For Windows users, the environment variable `KMP_DUPLICATE_LIB_OK` needs to be set to **TRUE**.
If the user would like to set environment variables in the Anaconda Powershell prompt (instead of using os.environ in the notebook), use the following command: `$env:KMP_DUPLICATE_LIB_OK="TRUE"` (note that the Anaconda Powershell prompt is different from the Anaconda prompt).

### Removing a conda environment

In case, for any reasons, you may need to re-install the conda packages from scratch, you can remove a conda environment this way:

```
conda deactivate
conda env remove -n echem-hessian
```

After removing a conda environment, it's also good to clean the cache:

```
conda clean --all
```

### Manual installation

It is possible to istall the conda packages without making use of the yml file provided. To do so, you have to first create a new conda environment and activate it:

```
conda create -n my-echem-env
conda activate my-echem-env
```

Then, install the required packages by running the command (Windows users):

```
conda install veloxchem msmpi py3dmol rdkit jupyterlab -c veloxchem -c conda-forge
```

or (Linux and macOS users):
```
conda install veloxchem py3dmol rdkit jupyterlab -c veloxchem -c conda-forge
```

### Known issues

- If you encounter ``InvalidArchiveError`` ([link to issue](https://github.com/conda/conda/issues/12235)), run ``conda clean --all`` and try again.

- If you encounter a ``DLL load failed`` error on Windows ([link to issue](https://github.com/conda/conda/issues/12161)), try the fix documented in [this link](https://github.com/conda/conda/issues/11795#issuecomment-1335666474).

- When using Python 3.11 you may need to set the environment variable ``PYDEVD_DISABLE_FILE_VALIDATION`` to ``1`` (see [this link](https://stackoverflow.com/a/75274358)).

## (2) Installation from source

Installation from source is only available for Linux and macOS operating systems, for Windows please use conda.

The main Python package needed to run the notebook is [VeloxChem](https://veloxchem.org/docs/intro.html). To build VeloxChem, the following are required:

- A C++ compiler compliant with the C++20 standard,
- An OpenMP library,
- Linear algebra libraries implementing the BLAS, LAPACK, and LAPACKE interfaces (e.g. OpenBLAS or MKL),
- An MPI library (e.g. MPICH),
- [Python](https://www.python.org/) >= 3.9 which includes the interpreter, the development header files, and the development libraries.

For macOS, the pre-requisites may be installed using Homebrew (see example below), while on Linux they can be installed using `sudo apt install`. For macOS, some flags may need to be set explicitly. We provide an example of installing pre-requisites on macOS below.

#### Pre-requisited: example for Intel macOS using Homebrew

```
brew install python
export PATH="/usr/local/bin:$PATH"
brew install libomp
brew install openblas
brew install mpich
```

You should not need to specify compiler flags by hand, but, in case compiling VeloxChem fails, set the following environment variables:

```
export CPPFLAGS="-I/usr/local/opt/libomp/include"
export CFLAGS="-Xpreprocessor -fopenmp $CPPFLAGS"
export CXXFLAGS="-Xpreprocessor -fopenmp $CPPFLAGS"
export LDFLAGS="-L/usr/local/opt/libomp/lib -lomp"
export CPPFLAGS="${CPPFLAGS} -I/usr/local/opt/openblas/include"
export LDFLAGS="${LDFLAGS} -L/usr/local/opt/openblas/lib"
export PKG_CONFIG_PATH="/usr/local/opt/openblas/lib/pkgconfig"
```


In the following, we will assume that the pre-requisites above have already been installed and are available.

### Create a virtual environment

We will carry out the installation in a Python virtual environment. Open a terminal and navigate to the folder where you intend to install the software.

Create and activate a Python virtual environment:

```
python3 -m venv echem-hessian-env
source echem-hessian-env/bin/activate
```

Install the pre-requisite Python packages:

```
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install mpi4py h5py pytest psutil geometric cmake pybind11-global scikit-build ninja
python3 -m pip install jupyterlab rdkit py3Dmol matplotlib
```

### Eigen and Libxc
Clone Eigen and set the environment variable `EIGEN_INCLUDE_DIR`:

```
git clone -b 3.4.0 https://gitlab.com/libeigen/eigen.git
export EIGEN_INCLUDE_DIR=/path/to/your/eigen
```

Install libxc 7.0.0:

```
git clone --branch 7.0.0 https://gitlab.com/libxc/libxc.git
cd libxc
mkdir build && cd build
cmake -DCMAKE_INSTALL_LIBDIR=lib -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/your/libxc ..
make && make test
make install
cd ../..
```

Note that the command above builds a light version of libxc and some related features in VeloxChem, such as time-dependent density functional theory (TDDFT) excited-state gradients, will not be available. For the full libxc build, see instructions [here](https://veloxchem.org/docs/installation.html#installing-on-cray-system). Please note that the full installation takes significantly more time compared to the light version.

### Compile VeloxChem

Clone the VeloxChem repository, configure, and install:

```
git clone https://github.com/VeloxChem/VeloxChem.git
cd VeloxChem
export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=<math_library> -DCMAKE_CXX_COMPILER=mpicxx"
export CMAKE_PREFIX_PATH=/path/to/your/libxc:$CMAKE_PREFIX_PATH
python3 -m pip install --no-build-isolation -v .
```
where `<math_library>` can be `MKL` or `OpenBLAS`, depending which linear algebra library you have installed.

Now you should be able to start the jupyter notebook:

```
jupyter-lab hessian_code_prototyping.ipynb
```

### Known issues
When building libxc you may encounter an error regarding the cmake version. In this case, you can follow the suggested fix by adding `-DCMAKE_POLICY_VERSION_MINIMUM=3.5` to the list of cmake flags.

For macOS, you may need to specifically add compiler flags for the OpenMP, BLAS, and MPI libraries. See example above. 

Other known issues related to installation on macOS and possible workarounds may be found [here](https://veloxchem.org/docs/installation.html#installing-on-macos).


### Note 

This README file has been last updated on 18/04/2025. For up-to-date installation instructions, please check [veloxchem.org](https://veloxchem.org/).
