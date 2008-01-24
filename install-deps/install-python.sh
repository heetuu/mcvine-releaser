  export PREF=$HOME/software
  wget http://www.python.org/ftp/python/2.4.3/Python-2.4.3.tgz
  rm -fr Python2.4.3
  tar zxvf ../dist/Python-2.4.3.tgz
  cd Python-2.4.3

  ./configure --prefix=${PREF}
  make
  make install
  cd ..

