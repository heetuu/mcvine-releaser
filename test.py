#!/usr/bin/env python

from utils.datastore import open
build_info = open('build_info')
export = build_info.get('export_root', 'EXPORT')

from build_envs import factory
ops = factory('mcvine', export)
from utils.envvars import perform
perform(ops)


def execute(cmd, where):
    import subprocess, shlex
    args = shlex.split(cmd)
    p = subprocess.Popen(args, cwd=where)

    while 1:
        rt = p.poll()
        p.communicate()
        if rt is None: continue
        break

    return rt

cxxfailed = execute(
    cmd = 'python run-cxx-tests.py',
    where='src/mcvine',
    )

pyunittestfailed = execute(
    # cmd = 'python run-unittests.py src/mcvine/packages/mcni',
    cmd = 'python run-unittests.py --exclude-dirs=sansmodel*,obsolete src/mcvine/packages',
    where = '.',
    )


if cxxfailed or pyunittestfailed:

    print
    print '='*60
    if cxxfailed:
        print '* c++ test failed'    
    if pyunittestfailed:
        print '* python unit tests failed'
    print '='*60
    
    import sys
    sys.exit(1)
