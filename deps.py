
externPackageInfo = {
    'numpy': "Numerical Python. see http://numpy.scipy.org/",
    'cctbx': "crystallography toolbox",
    'McStas': "riso McStas",
    }


packages = [
    'numpy',
    'cctbx',
    'McStas',
    ]

descriptions = {
    'numpy': "Numerical Python. see http://numpy.scipy.org/",
    'cctbx': 'Crystallography tool box',
    'McStas': 'Risoe McStas',
    }


def install( software ):
    global installers
    installers[ software ]()
    return


installers = {}

from utils.installers import get as get_installer

installers[ 'numpy' ] = get_installer( 'numpy', 'src' )
installers[ 'cctbx' ] = get_installer( 'cctbx', 'src' )
installers[ 'McStas' ] = get_installer( 'McStas', 'src' )

