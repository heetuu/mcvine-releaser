import os

pyre_root = os.environ['PYRE_DIR']
etc = os.path.join( pyre_root, 'etc' )

_SYSTEM_ROOT = etc
_USER_ROOT = os.path.join(os.path.expanduser('~'), '.pyre')
_LOCAL_ROOT = [ '.' ]

