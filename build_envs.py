#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2010 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

try:
    from utils.paths.boostpython import paths as boostpython_paths
    bproot = boostpython_paths.root
except:
    bproot = '$deps'

template = """
export_root=%(export_root)s
deps=$export_root/deps

export %(package)s_DIR=$export_root

export PYRE_DIR=$export_root
export PATH=$export_root/bin:$deps/bin:$PATH
export LD_LIBRARY_PATH=$export_root/lib:$deps/lib:$LD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$export_root/lib:$deps/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=$export_root/modules:$deps/python:$PYTHONPATH
"""
template += """
export BOOSTPYTHON_LIBDIR=%s/lib
export BOOSTPYTHON_INCDIR=%s/include
""" % (bproot, bproot)


from utils.scripts.build_envs import createMain
main = createMain('mcvine', template)

if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
