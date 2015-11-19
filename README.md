**_This is obsolete. Building release is now done with the mcvine source code using cmake_**

[![Build Status](https://travis-ci.org/mcvine/releaser.svg?branch=master)](https://travis-ci.org/mcvine/releaser)

# The facility to build mcvine
## Build instructions
### Install prerequsites

See Dockerfiles in docker/ sub-directory for hints on how to install dependencies.

### Build

  $ ./build.py

## Organization

* deps.py: information of external dependencies 
* packages/: information of included packages and their dependencies
* src/: source directory
* docker/: docker instructions to build mcvine dependencies, build mcvine, and test mcvine
* buildbot/: buildbot configurations
* utils/: utilities for this releaser. checked out danse-inelastic/build_utils
