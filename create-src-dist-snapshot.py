#!/usr/bin/env python

# create a snapshot of source distribution and upload it

def execute(cmd):
    import os
    if os.system(cmd):
        raise RuntimeError, "%s failed"
    return


def main():
    name = 'mcvine-src-dist'
    cmd = "./create-src-dist.py %s" % name
    execute(cmd)
    # upload to danse repository
    dest = "login.cacr.caltech.edu:projects/danse/packages/dev_danse_us/"
    cmd = 'scp %s.tgz %s' % (name, dest)
    execute(cmd)
    return


if __name__ == '__main__': main()

