from pythia_original import path, sub_modules, deps, checkoutCmd, updateCmd

def patch( dest ):
    from pythia_original import patch
    patch( dest )
    override_prefix_py( dest )
    return
    

prefix_py_content = '''
from softwareinstallationinfodb import info
pythiainfo = info('pythia')
root = pythiainfo.root
import os
etc = os.path.join( root, 'etc' )
_SYSTEM_ROOT = etc
_USER_ROOT = os.path.join(os.path.expanduser('~'), '.pyre')
_LOCAL_ROOT = [ '.' ]
'''
def override_prefix_py( dest ):
    import os
    dst = os.path.join( dest, "packages", "pyre", "pyre", 
                        "inventory", "odb", "prefix.py" )
    open(dst, 'w').write( prefix_py_content)
    return

