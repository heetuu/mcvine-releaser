  export PREF=$HOME/software
  wget ftp://ftp.ncsa.uiuc.edu/HDF/HDF5/h4toh5/src/h4h5tools-1.2.tar.gz
  rm -fr h4h5tools-1.2
  tar zxvf h4h5tools-1.2.tar.gz
  cd h4h5tools-1.2
  export LD_LIBRARY_PATH=$PREF/lib:$LD_LIBRARY_PATH
  CC=$PREF/bin/h4cc ./configure --prefix=$PREF --with-hdf5=$PREF
  make
  make install
  cd ../..

