
packages = [
    'py_numpy',
    'py_psutil',
    'boostpython',
    # 'HDF5',
    'py_h5py',
    # 'mpich2',
    'gsl',
    #'wxPython',
    #'McStas',
    # danse.ins packages
    ]

descriptions = {
    'py_numpy': "Numerical Python. see http://numpy.scipy.org/",
    'py_psutil': 'psutil python module',
    'boostpython': 'Boostpython',
    'HDF5': 'HDF5',
    'py_h5py': 'python binding of hdf5',
    'mpich2': 'mpich2',
    'McStas': 'Risoe McStas',
    'wxPython': 'wx python',
    'gsl': 'GNU scientific library',
    }


def install( software ):
    global installers
    installers[ software ]()
    return


installers = {}

from utils.installers import get as get_installer

installers[ 'py_numpy' ] = get_installer( 'py_numpy', 'src' )
installers[ 'py_psutil' ] = get_installer( 'py_psutil', 'src')
installers[ 'boostpython' ] = get_installer( 'boostpython', 'src' )
installers[ 'HDF5' ] = get_installer( 'HDF5', 'src' )
installers[ 'py_h5py' ] = get_installer( 'py_h5py', 'src' )
installers[ 'mpich2' ] = get_installer( 'mpich2', 'src' )
installers[ 'wxPython' ] = get_installer( 'wxPython', 'src' )
installers[ 'gsl' ] = get_installer( 'gsl', 'src' )
#installers[ 'McStas' ] = get_installer( 'McStas', 'src' )

