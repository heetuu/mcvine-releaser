
packages = [
    'py_numpy',
    'boostpython',
    #'McStas',
    ]

descriptions = {
    'py_numpy': "Numerical Python. see http://numpy.scipy.org/",
    'boostpython': 'Boostpython',
    #'McStas': 'Risoe McStas',
    }


def install( software ):
    global installers
    installers[ software ]()
    return


installers = {}

from utils.installers import get as get_installer

installers[ 'py_numpy' ] = get_installer( 'py_numpy', 'src' )
installers[ 'boostpython' ] = get_installer( 'boostpython', 'src' )
#installers[ 'McStas' ] = get_installer( 'McStas', 'src' )

