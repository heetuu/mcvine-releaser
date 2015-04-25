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

def get_bp_info(dottools):
    lines = open(dottools)
    inc_sig = "export BOOSTPYTHON_INCDIR="
    lib_sig = "export BOOSTPYTHON_LIBDIR="
    for line in lines:
        if line.startswith(inc_sig):
            inc = line[len(inc_sig):].strip().strip("'")
            continue
        if line.startswith(lib_sig):
            lib = line[len(lib_sig):].strip().strip("'")
        continue
    return inc, lib


from utils.scripts.build_envs import createMain, createEnvVarOps

def factory(package, export):
    ops = createEnvVarOps(package, export)
    from utils.envvars.operations import Set
    bp_inc, bp_lib = get_bp_info('src/dottools')
    import pdb; pdb.set_trace()
    ops.append(Set('BOOSTPYTHON_INCDIR', bp_inc))
    ops.append(Set('BOOSTPYTHON_LIBDIR', bp_lib))
    return ops

main = createMain('mcvine', envvarops_factory=factory )


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
