# -*- Makefile -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2004  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

PROJECT = simulation-bundle

# directory structure

BUILD_DIRS = \
	pythia-0.8\
	pyregui\
	array_kluge\
	stdVector\
	hdf5fs\
	nx5\
	histogram\
	measurement\
	instrument\
	reduction\
	pyregui\
	cctbx_adpt\
	simulation\
	mcstas\

OTHER_DIRS = \

RECURSE_DIRS = $(BUILD_DIRS) $(OTHER_DIRS)

#--------------------------------------------------------------------------
#

all:
	BLD_ACTION="all" $(MM) recurse

distclean::
	BLD_ACTION="distclean" $(MM) recurse

clean::
	BLD_ACTION="clean" $(MM) recurse

tidy::
	BLD_ACTION="tidy" $(MM) recurse

docs::
	BLD_ACTION="docs" $(MM) recurse

export::
	BLD_ACTION="export" $(MM) recurse

test::
	BLD_ACTION="test" $(MM) recurse

# version
# $Id: Make.mm 616 2007-05-13 18:05:03Z linjiao $

# End of file
