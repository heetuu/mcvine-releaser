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
    bproot = None


from utils.scripts.build_envs import createMain, createEnvVarOps

def factory(package, export):
    ops = createEnvVarOps(package, export)
    from utils.envvars.operations import Set
    import os
    global bproot
    if bproot is None:
        deps = os.path.join(export, 'deps')
        bproot = deps
    bp_inc = os.path.join(bproot, 'include')
    bp_lib = os.path.join(bproot, 'lib')
    ops.append(Set('BOOSTPYTHON_INCDIR', bp_inc))
    ops.append(Set('BOOSTPYTHON_LIBDIR', bp_lib))
    return ops

main = createMain('mcvine', envvarops_factory=factory )


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
