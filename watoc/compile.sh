export SKBUILD_CONFIGURE_OPTIONS="-DVLX_LA_VENDOR=OpenBLAS -DCMAKE_CXX_COMPILER=mpicxx"
export XTBHOME=/opt/miniconda3/envs/vlxenv-md/bin/xtb
export CMAKE_ARGS="-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=11.0"

VLX_NUM_BUILD_JOBS=10 python3 -m pip install . -v --no-build-isolation
