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


def main():
    from packages import packageNames, checkout
    from directory_structure import tree
    srcRt = tree.search( "sources" ).path
    checkout(packageNames, srcRt)
    #import dereference
    #dereference.dereference_recursively( 'src' )
    return


if __name__ == "__main__": main()



# version
__id__ = "$Id$"

# End of file 
