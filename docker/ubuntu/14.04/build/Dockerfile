FROM linjiao/mcvine-ubuntu-deps

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

# prepare 
RUN mkdir -p /opt
WORKDIR /opt
RUN git clone https://github.com/heetuu/mcvine-releaser.git mcvine

# build
WORKDIR /opt/mcvine
RUN BOOSTPYTHON_DIR=/usr BOOSTPYTHON_INCDIR=/usr/include BOOSTPYTHON_LIBDIR=/usr/lib/x86_64-linux-gnu ./build.py
