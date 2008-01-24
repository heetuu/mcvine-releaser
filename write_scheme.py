
import sys, os

def create_install_info_py( bin, lib, include, python, share, etc, path = "install_info.py" ):
    # create a install_info.py that has information about the
    # installation scheme
    text = "bin = '%s'\n" % bin
    text += "lib = '%s'\n" % lib
    text += "include = '%s'\n" % include
    text += "python = '%s'\n" % python
    text += "share = '%s'\n" % share
    text += "etc = '%s'\n" % etc
    open(path, 'w').write( text )
    return


def create_envs_sh( bins, libs, pythons, path = "evns.sh" ):
    # create a "envs.sh" that add bins,libs,pythons to
    # corresponding paths
    text = "export PATH=%s:$PATH\n" % ":".join( [ str(bin) for bin in bins ] )
    
    libs = ':'.join( [ str(lib) for lib in libs ] )
    if sys.platform == "darwin":
        text += "export DYLD_LIBRARY_PATH=%s:$DYLD_LIBRARY_PATH\n" % libs
    else:
        text += "export LD_LIBRARY_PATH=%s:$LD_LIBRARY_PATH\n" % libs
        pass
    text += "export PYTHONPATH=%s:$PYTHONPATH\n" % \
            ':'.join( [ str(python) for python in pythons ] )
    
    open( path, 'w' ).write(text)
    return


def mkdir( p ):
    import os
    try: os.makedirs(p)
    except:
        if not os.path.isdir(p) : raise
        pass
    return


def write_scheme( scheme ):
    bin = scheme['bin']
    include = scheme['include']
    lib = scheme['lib']
    python = scheme['python']
    share = scheme['share']
    etc = scheme['etc']
    
    for p in [bin, include, lib, python, share, etc]: mkdir(p)

    iipy = os.path.join(python, "install_info.py")
    create_install_info_py( bin, lib, include, python, share, etc, path = iipy )
    
    es = os.path.join(bin, "envs.sh")
    create_envs_sh( [bin], [lib], [python], path = es)
    return


