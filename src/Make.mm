PROJECT = mcvine


PROJ_TIDY += *.log *.tmp

# directory structure


BUILD_DIRS = \
	ctrl/config/branches/with_doxygen_and_docbook_support \
	pyre/branches/patches-from-jiao \
	pyregui/trunk \
	inelastic/dsm \
	inelastic/numpyext \
	inelastic/bpext \
	pyregui/trunk/luban \
	histogram/trunk \
	inelastic/crystal \
	hdf5fs/trunk \
	nx5/trunk \
	instrument/trunk \
	common/dataObjects/sample/branches/sampleassembly \
	MCViNE/trunk \
	sans/trunk/sansmodels/src \



RECURSE_DIRS = $(BUILD_DIRS)

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

# version
# $Id: Make.mm 1363 2007-07-29 14:24:24Z linjiao $

# End of file
