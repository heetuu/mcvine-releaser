from utils.packages.dsm import *
from utils.package import repoutils

# old: svn
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

# git
reponame = "dsm"
branch = "master"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
