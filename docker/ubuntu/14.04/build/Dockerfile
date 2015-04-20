FROM linjiao/mcvine-ubuntu-deps

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

WORKDIR /opt/mcvine
RUN BOOSTPYTHON_DIR=/usr BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib/x86_64-linux-gnu ./build.py
