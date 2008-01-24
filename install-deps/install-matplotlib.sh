  export PREF=$HOME/software
  # Matplotlib
  #   http://matplotlib.sourceforge.net/
  # http://superb-west.dl.sourceforge.net/sourceforge/matplotlib/matplotlib-0.87.4.tar.gz
  # Looks like 0.87.4 supports numpy
  #   svn co https://svn.sourceforge.net/svnroot/matplotlib matplotlib

  wget http://superb-west.dl.sourceforge.net/sourceforge/matplotlib/matplotlib-0.87.4.tar.gz
  rm -fr matplotlib-0.87.4
  tar zxvf matplotlib-0.87.4.tar.gz
  cd matplotlib-0.87.4

  # It'll try to use Tk if it sees it there, which is both ugly if it compiled
  # at all which it doesn't.
  cd matplotlib-0.87.4
  sed 's/^BUILD_TKAGG.*$/BUILD_TKAGG=0/' < setup.py > setup.py.new
  rm -f setup.py
  mv setup.py.new setup.py

  python setup.py build
  python setup.py install
  cd ..

