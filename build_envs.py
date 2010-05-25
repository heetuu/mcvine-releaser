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

template = """
export_root=%(export_root)s
deps=$export_root/deps

export %(package)s_DIR=$export_root
export MCSTAS_COMPONENT_LIBDIR=$export_root/share/mcstas2/McStas-Components

export PYRE_DIR=$export_root
export PATH=$export_root/bin:$deps/bin:$PATH
export LD_LIBRARY_PATH=$export_root/lib:$deps/lib:$LD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$export_root/lib:$deps/lib:$DYLD_LIBRARY_PATH
export PYTHONPATH=$export_root/modules:$deps/python:$PYTHONPATH

export BOOSTPYTHON_LIBDIR=$deps/lib
export BOOSTPYTHON_INCDIR=$deps/include
"""

from utils.scripts.build_envs import createMain
main = createMain('mcvine', template)

if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
