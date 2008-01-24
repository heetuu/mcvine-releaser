  export PREF=$HOME/software
  wget http://easynews.dl.sourceforge.net/sourceforge/wxpython/wxPython-src-2.6.3.3.tar.bz2

  rm -fr wxPython-src-2.6.3.3
  tar jxvf wxPython-src-2.6.3.3.tar.bz2
  cd wxPython-src-2.6.3.3
  ./configure --enable-monolithic --prefix=${PREF}

  make
  make -C contrib/src/animate
  make -C contrib/src/gizmos
  make -C contrib/src/stc
  make install
  make -C contrib/src/animate install
  make -C contrib/src/gizmos install
  make -C contrib/src/stc install

  cd wxPython
  export PATH=$PREF/bin:$PATH
  Args="BUILD_GLCANVAS=0"

  # Does --inplace do something useful?
  python setup.py build_ext --inplace $Args
  # Do not specify --root= here; it's picking it up from somewhere else
  python setup.py install $Args
  cd ../..

