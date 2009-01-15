
packages = [
    'py_numpy',
    'boostpython',
    'HDF5',
    #'wxPython',
    #'mpich2',
    #'McStas',
    ]

descriptions = {
    'py_numpy': "Numerical Python. see http://numpy.scipy.org/",
    'boostpython': 'Boostpython',
    'HDF5': 'HDF 5',
    'mpich2': 'mpich2',
    'McStas': 'Risoe McStas',
    'wxPython': 'wx python',
    }


def install( software ):
    global installers
    installers[ software ]()
    return


installers = {}

from utils.installers import get as get_installer

installers[ 'py_numpy' ] = get_installer( 'py_numpy', 'src' )
installers[ 'boostpython' ] = get_installer( 'boostpython', 'src' )
installers[ 'HDF5' ] = get_installer( 'HDF5', 'src' )
installers[ 'mpich2' ] = get_installer( 'mpich2', 'src' )
installers[ 'wxPython' ] = get_installer( 'wxPython', 'src' )
#installers[ 'McStas' ] = get_installer( 'McStas', 'src' )

