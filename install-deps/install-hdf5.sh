#hdf5 by default does not build c++ shared library. So
#please be careful when you are building hdf5. Follow
#the commands in the script carefully.
  export PREF=$HOME/software
  wget ftp://ftp.hdfgroup.org/HDF5/current/src/hdf5-1.6.5.tar.gz
  rm -fr hdf5-1.6.5
  tar zxvf hdf5-1.6.5.tar.gz
  cd hdf5-1.6.5
  ./configure --prefix=$PREF --enable-cxx
  make
  make install
  #the following is for creating shared library 
  cd c++/src
  cat Makefile | sed 's/^CFLAGS.*$/CFLAGS= -O2 -fPIC/' | sed 's/^CXXFLAGS.*$/CXXFLAGS= -O2 -fPIC/' | sed '/^LT_LINK_LIB/ s/static/shared/' | sed '/^LT_LINK_EXE/s/static/shared/' > Makefile.new
  mv Makefile Makefile.unsedded
  mv Makefile.new Makefile
  make clean
  make
  make install
  cd ../..

