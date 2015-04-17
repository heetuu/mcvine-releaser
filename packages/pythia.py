name = "pyre"
deps = ("config",)

from utils.package import repoutils

reponame = 'pyre'
# svn
# branch = "pythia-0.8"
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

branch = "master"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)


def patch( dest ):
    curdir = os.path.abspath( os.path.dirname( __file__ ) )
    patches_dir = os.path.join( curdir, "pythia-patches" )
    copy_prefix_py( patches_dir, dest )
    return
    

def copy_prefix_py( patches_dir, dest ):
    import os
    import shutil
    src = os.path.join( patches_dir, "prefix.py" )
    dst = os.path.join( dest, "packages", "pyre", "pyre", 
                        "inventory", "odb", "prefix.py" )
    print "copy %s to %s" % (src, dst)
    shutil.copy( src, dst )

    src = os.path.join( patches_dir, "pyre-inventory-odb-Make.mm" )
    dst = os.path.join( dest, "packages", "pyre", "pyre", 
                        "inventory", "odb", "Make.mm" )
    print "copy %s to %s" % (src, dst)
    os.system( 'rm -f %s' % dst)
    shutil.copy( src, dst )
    return


import os
