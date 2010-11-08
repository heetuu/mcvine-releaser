#!/usr/bin/env python

from utils.datastore import open
build_info = open('build_info')
export = build_info.get('export_root', 'EXPORT')

from utils.scripts.build_envs import createEnvVarOps
ops = createEnvVarOps('mcvine', export)
from utils.envvars import perform
perform(ops)

import subprocess, shlex
cmd = 'python run-cxx-tests.py'
args = shlex.split(cmd)
p = subprocess.Popen(args, cwd='src/mcvine')

while 1:
    rt = p.poll()
    p.communicate()
    if rt is None: continue
    break

if rt: 
    import sys
    sys.exit(rt)
