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
    
    options, args = parser.parse_args()
    
    if len(args) > 1: raise NotImplementedError
    if len(args) == 1:
        path = args[0]
    else:
        path = os.curdir
        
    exclude_dirs = options.exclude_dirs
    if exclude_dirs:
        exclude_dirs = exclude_dirs.split(',')
    
    from utils.unittest.run_tests import runtests, printRsult
    result = runtests(path, exclude_dirs=exclude_dirs)
    printRsult(result)
    exitonerror(result)
    
    return


if __name__ == '__main__': main()
