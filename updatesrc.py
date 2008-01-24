#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2006  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# script to update release


def main():
    from packages import packageNames, update
    from directory_structure import tree
    srcRt = tree.search( "sources" ).path
    update(packageNames, srcRt)
    return


if __name__ == "__main__": main()



# version
__id__ = "$Id$"

# End of file 
