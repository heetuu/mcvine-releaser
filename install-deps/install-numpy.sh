  export PREF=$HOME/software
  # http://superb-east.dl.sourceforge.net/sourceforge/numpy/numpy-1.0b1.tar.gz
  wget http://superb-east.dl.sourceforge.net/sourceforge/numpy/numpy-1.0b1.tar.gz
  tar zxvf numpy-1.0b1.tar.gz
  cd numpy-1.0b1
  python setup.py build
  python setup.py install
  cd ..
