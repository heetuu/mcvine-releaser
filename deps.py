
packages = [
    'numpy',
    'boostpython',
    #'McStas',
    ]

descriptions = {
    'numpy': "Numerical Python. see http://numpy.scipy.org/",
    'boostpython': 'Boostpython',
    #'McStas': 'Risoe McStas',
    }


def install( software ):
    global installers
    installers[ software ]()
    return


installers = {}

from utils.installers import get as get_installer

installers[ 'numpy' ] = get_installer( 'numpy', 'src' )
installers[ 'boostpython' ] = get_installer( 'boostpython', 'src' )
#installers[ 'McStas' ] = get_installer( 'McStas', 'src' )

