  export PREF=$HOME/software
  wget http://cci.lbl.gov/cctbx_build/results/2007_04_04_2342/cctbx_bundle.tar.gz

  rm -fr cctbx
  mkdir cctbx
  cd cctbx
  tar xvfz ../cctbx_bundle.tar.gz
  mkdir cctbx_build
  cd cctbx_build
  python ../cctbx_sources/libtbx/configure.py mmtbx
  source setpaths.sh
  libtbx.scons

  export PATH=$PREF/bin:$PATH
  cd ../..

