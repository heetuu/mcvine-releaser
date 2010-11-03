#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def build(export_root):
    import sys, os
    pwd = os.path.abspath( os.curdir )

    import sys
    sys.path = [pwd] + sys.path

    from utils.build import build_release, clean_up
    build_release( pwd, export_root=export_root)
    return


def main():
    import sys, os, shlex

    from utils.datastore import open
    build_info = open('build_info')
    
    if len(sys.argv) == 2:
        export_root = sys.argv[1]
    else:
        if build_info.get('export_root'):
            export_root = build_info['export_root']
        else:
            export_root = os.path.abspath('EXPORT')

    build_info['export_root'] = export_root
    
    cmd = 'python -c "import build; build.build(%r)"' % export_root
    args = shlex.split(cmd)

    deps_root = os.path.join(export_root, 'deps')
    env = os.environ.copy()
    env['PATH'] = '%s:%s' % (
        os.path.join( deps_root, 'bin' ), env['PATH'] )
    env['LD_LIBRARY_PATH'] = '%s:%s' % (
        os.path.join( deps_root, 'lib' ), env.get('LD_LIBRARY_PATH') or '' )
    env['DYLD_LIBRARY_PATH'] = '%s:%s' % (
        os.path.join( deps_root, 'lib' ), env.get('DYLD_LIBRARY_PATH') or '' )
    env['PYTHONPATH'] = '%s:%s' % (
        os.path.join( deps_root, 'python' ), env.get('PYTHONPATH', '') )
    import subprocess
    p = subprocess.Popen(args, env=env)
    while p.poll() is None:
        p.communicate()


if __name__ == '__main__': main()


# version
__id__ = "$Id$"

# End of file 
