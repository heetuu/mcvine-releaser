FROM linjiao/mcvine-centos-deps:6a

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image to build MCViNE"

WORKDIR /opt/mcvine
RUN PATH=/opt/bin:$PATH BOOSTPYTHON_INCDIR=/opt/include BOOSTPYTHON_LIBDIR=/opt/lib GSL_INCDIR=/usr/include GSL_LIBDIR=/usr/lib64  /opt/bin/python2.7 ./build.py
