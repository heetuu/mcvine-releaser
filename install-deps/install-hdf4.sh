  export PREF=$HOME/software
  wget ftp://ftp.ncsa.uiuc.edu/HDF/HDF/HDF_Current/src/HDF4.2r1.tar.gz
  rm -fr HDF4.2r1
  tar zxvf  HDF4.2r1.tar.gz
  cd  HDF4.2r1
  ./configure --prefix=$PREF 
  make
  make install
  cd ../..

