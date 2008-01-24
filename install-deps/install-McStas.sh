  version=1.8
  export PREF=$HOME/software
  wget http://www.mcstas.org/downloads/mcstas-${version}-src.tar.gz
  rm -fr mcstas
  tar zxvf mcstas-${version}-src.tar.gz
  cd mcstas-${version}
  ./configure --prefix=$PREF
  make
  make install
  cd ../..

