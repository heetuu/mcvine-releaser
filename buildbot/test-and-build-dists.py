#!/usr/bin/env python


# run test, and if test succeed, build distributions
# this script must be run from the root of the mcvine releaser

def main():
    import os
    cmd = './test.py'
    if os.system(cmd):
        import sys
        sys.exit(1)

    cmd = './create-src-dist-snapshot.py'
    if os.system(cmd):
        raise RuntimeError, "%s failed"

    return


if __name__ == '__main__': main()
