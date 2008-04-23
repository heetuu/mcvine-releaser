#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                       (C) 2006 All Rights Reserved 
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# This directory contains python modules describing packages to be included
# in the software.
#
# __init__.py: gather global information about packages. don't touch
# bundles.py: packages are grouped into bundles. change it when new packages
#             are added or when bundles need to be restructured
# defaults.py: default packages to be installed
# other modules: each module contains information about a specific package
#
#   setupScript = name of distutils-adpt setup script
#   path = path in 'src' directory
#   deps = names of dependencies
#   checkoutCmd = command to check out the package from repository

import sys, os
## f = __file__
## d = os.path.dirname( f )
## p = os.path.abspath( os.path.join( d, '..', '..') )
## sys.path = [p] + sys.path
## del f,d,p

from bundles import *

from defaults import *


packageSequence = []
for name in bundleNames: packageSequence += bundleInfo[name]

#alias
packageNames = packageSequence


def createTable(packageNames):
    import sys, os
    t = {}
    for name in packageNames:
        modname = name.replace( '-', '_' )
        m = __import__( "packages.%s" % modname, globals(), locals(), [""] )
        t[name] = m.__dict__
        continue
    return t
                    
        

#a dictionary of infos of packages
#   name: (setup script name,  relative path of the package, dependencies)
packageInfoTable = createTable( packageNames )
    


def checkout( packageNames, dest ):
    """check out packages at "dest" directory"""
    for package in packageNames:
        cmd = "cd %s; " % dest
        cocmd = packageInfoTable[ package ]['checkoutCmd']
        if cocmd:
            cmd += cocmd
            if os.system(cmd): print "Unable to check out %s" % package
            pass
        patch(package, dest)
        continue
    return


def update( packageNames, dest ):
    """update packages at "dest" directory"""
    for package in packageNames:
        info = packageInfoTable[ package ]
        p = os.path.join( dest, info['path'] )
        cmd = "cd %s; " % p
        udcmd = info['updateCmd']
        if udcmd:
            cmd += udcmd
            if os.system(cmd): print "Unable to update %s" % package
            pass
        patch(package, dest)
        continue
    return


def patch( packageName, dest ):
    print 'patching %s' % packageName
    patch = packageInfoTable[ packageName ].get( 'patch' )
    path = packageInfoTable[ packageName ][ 'path' ]
    dest = os.path.join( dest, path )
    if patch: patch(dest)
    else: "No patch for package %s" % packageName
    return



# version
__id__ = "$Id$"


# End of file 
