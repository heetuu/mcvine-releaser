#cctbx package
#Please revise the following line to reflect the installation
#tree of cctbx
export CCTBX_ROOT=/home/linjiao/install/cctbx/2005_04_29
export CCTBX_BUILD=${CCTBX_ROOT}/cctbx_build
export CCTBX_SOURCES=${CCTBX_ROOT}/cctbx_sources
export CCTBX_LIBDIR=${CCTBX_BUILD}/lib
export CCTBX_INCDIR=${CCTBX_ROOT}/include
export CCTBX_BUILD_INCDIR=${CCTBX_BUILD}/include
export LD_LIBRARY_PATH=${CCTBX_LIBDIR}:$LD_LIBRARY_PATH
export PYTHONPATH=${CCTBX_SOURCES}/boost_adaptbx:${CCTBX_SOURCES}/scitbx:${CCTBX_SOURCES}/cctbx:${CCTBX_SOURCES}/iotbx:${CCTBX_LIBDIR}:${CCTBX_SOURCES}/libtbx:${PYTHONPATH}:${CCTBX_BUILD}


