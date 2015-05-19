# The facility to build mcvine
## Build instructions
### Install prerequsites

See Dockerfiles in docker/ sub-directory for hints on how to install dependencies.

### Build

  $ ./build.py

## Organization

* deps.py: information of external dependencies 
* packages/: information of included packages
* src/: source directory
* docker/: docker instructions to build mcvine dependencies, build mcvine, and test mcvine
* buildbot/: buildbot configurations
* utils/: utilities for this releaser. checked out heetuu/build_utils
