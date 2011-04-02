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
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("", "--exclude-dirs", dest="exclude_dirs",
                      help = 'patterns to exclude directories',)
    parser.add_option('', '--skip-long-tests', dest='skip_long_tests',
                      action = 'store_true',
                      help = 'when on, skip tests that take long time to run',
                      )
    
    options, args = parser.parse_args()
    
    if len(args) > 1: raise NotImplementedError
    if len(args) == 1:
        path = args[0]
    else:
        path = os.curdir
        
    exclude_dirs = options.exclude_dirs
    if exclude_dirs:
        exclude_dirs = exclude_dirs.split(',')

    skip_long_tests = options.skip_long_tests
    
    from utils.unittest.run_tests import runtests, printResult
    result = runtests(path, exclude_dirs=exclude_dirs, skip_long_tests=skip_long_tests)
    printResult(result)
    exitonerror(result)
    
    return


if __name__ == '__main__': main()
