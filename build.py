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
    import sys, os
    pwd = os.path.abspath( os.curdir )

    import sys
    sys.path = [pwd] + sys.path

    from utils.build import build_release, clean_up
    build_release( pwd )

    # create envs.sh
    os.system('./create-envssh.py')
    os.system('./create-dotmcvine.py')
    return


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
