#!/usr/bin/env python


# create source distribution

# assumption:
#  - unix
#  - bash
#  - python
#  - tar
#  - git

import os, sys


def create(name):
    if name.find('/') != -1:
        raise ValueError, "bad directory name %s" % name
    if os.path.exists(name):
        raise IOError, "%s already exists" % name
    cmd = ['git clone https://github.com/mcvine/releaser %s' % name]
    cmd.append('cd %s' %name)
    cmd.append('./getsrc.py')
    cmd = ' && '.join(cmd)
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd

    # remove source control files, .pyc files etc
    from utils.build import clean_up
    clean_up(name)
    
    # remove example. they are distributed separately
    cmd = 'rm -rf %s/src/mcvine/examples' % name
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd
    
    # create tar ball
    cmd = 'tar -czf %s.tgz %s' % (name, name)
    if os.system(cmd):
        raise RuntimeError, "%s failed" % cmd
    
    import shutil
    shutil.rmtree(name)
    
    return


if __name__ == '__main__': 
    create(sys.argv[1])
