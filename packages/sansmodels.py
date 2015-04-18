from utils.packages.sansmodels import *

from utils.package import repoutils

# old: svn
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

# git
reponame = "sansmodels"
branch = "master"
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
