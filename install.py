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


help = """Usage:

 $ install.py <path>
"""


def main():
    import sys
    if len(sys.argv) != 2:
        print help
        sys.exit(2)
        raise
    
    path = sys.argv[1]

    from build import main
    main()

    import os
    pwd = os.path.abspath( os.curdir )
    export = os.path.join( pwd, 'EXPORT' )

    from utils.install import copy_all, build_envs_sh
    copy_all( export, path )

    build_envs_sh( path )
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
