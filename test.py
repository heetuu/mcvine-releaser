#!/usr/bin/env python


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


def runall(skip_long_tests=False):
    # where is the <export>?
    from utils.datastore import open
    build_info = open('build_info')
    export = build_info.get('export_root', 'EXPORT')

    # set up env vars
    from build_envs import factory
    ops = factory('mcvine', export)
    from utils.envvars import perform
    perform(ops)

    # cxx tests
    cxxfailed = execute(
        cmd = 'python run-cxx-tests.py src/mcvine',
        where='.',
        )

    # python unit tests
    cmd = 'python run-unittest.py '
    args = "-r --exclude-dirs=sansmodel*,obsolete --log=log.verbose".split()
    if skip_long_tests: args.append(' --skip-long-tests')
    args.append("src/mcvine/packages")
    cmd += ' '.join(args)
    pyunittestfailed = execute(
        # cmd = 'python run-unittests.py src/mcvine/packages/mcni',
        cmd = cmd,
        where = '.',
        )

    #
    failed = cxxfailed or pyunittestfailed

    # report
    if failed:
        print
        print '='*60
        if cxxfailed:
            print '* c++ test failed'    
        if pyunittestfailed:
            print '* python unit tests failed'
        print '='*60

    else:
        print
        print '='*60
        print 'All tests passed'
        
    return failed



def main():
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option(
        "", "--skip-long-tests", 
        action="store_true", dest="skip_long_tests",
        )
    (options, args) = parser.parse_args()
    assert len(args) == 0
    
    failed = runall(**vars(options))

    if failed:
        import sys
        sys.exit(1)

    return


if __name__ == '__main__': main()
