#!/usr/bin/env bash

. src/dottools
EXPORT=`python -c "from utils.datastore import open; print open('build_info')['export_root']"`
. $EXPORT/bin/envs.sh
export DV_DIR=$PWD/src
mcvine-compile-all-mcstas-components
