FROM fedora:21

MAINTAINER "Jiao Lin <linjiao@caltech.edu>"

LABEL Description="image prepared for buildindg MCViNE"

# installation of basic software and dependencies
# 
# dependencies: packages
RUN yum install -y python python-devel numpy python-psutil h5py
# dependencies: c libs
RUN yum install -y install gsl gsl-devel
# dependencies: boost python
RUN yum install -y boost-devel boost-python
# dev
RUN yum install -y git gcc-c++ make

