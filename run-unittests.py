#!/usr/bin/env python


'''
given a directory, recursively run all unittests and gather statistics
'''

import sys, os


def exitonerror(result):
    if result.errors or result.failures:
        sys.exit(1)
    return


def main():
    argv = sys.argv
    if len(argv) > 2: raise NotImplementedError
    if len(argv) == 2:
        path = argv[1]
    else:
        path = os.curdir

    from utils.unittest.run_tests import runtests, printRsult
    result = runtests(path)
    printRsult(result)
    exitonerror(result)
    return


if __name__ == '__main__': main()
