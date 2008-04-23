# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PROJECT = pyre
PACKAGE = inventory/odb

EXPORT_ETCDIR = ${EXPORT_ROOT}/etc


#--------------------------------------------------------------------------
#

all: export

#--------------------------------------------------------------------------
# export

EXPORT_PYTHON_MODULES = \
    Curator.py \
    Descriptor.py \
    Inventory.py \
    Registry.py \
    prefix.py \
    __init__.py


export::  export-package-python-modules


# version
# $Id: Make.mm,v 1.1.1.1 2005/03/08 16:13:43 aivazis Exp $

# End of file
