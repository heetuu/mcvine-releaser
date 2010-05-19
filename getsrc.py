#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# script to check out sources

from packages import packageNames, checkout

def get(names):
    from directory_structure import tree
    srcRt = tree.search( "sources" ).path
    if not names: names = packageNames
    checkout(names, srcRt)
    #import dereference
    #dereference.dereference_recursively( 'src' )
    return


def main():
    import sys
    argv = sys.argv
    names = argv[1:]
    get(names)
    return


if __name__ == "__main__": main()



# version
__id__ = "$Id$"

# End of file 
