#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def main():
    # build
    from utils.scripts.build import main
    print ">>> building mcvine"
    main()

    # build envs.sh
    from build_envs import main
    print ">>> building environment-setup script"
    main()

    # build all mcstas components
    print ">>> building all mcvine-wrapped mcstas components"
    import os
    os.system('./build_all_mcstas_components.sh')
    return


if __name__ == '__main__': main()

# version
__id__ = "$Id$"

# End of file 
