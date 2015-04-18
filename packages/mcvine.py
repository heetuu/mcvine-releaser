from utils.packages.mcvine import *

from utils.package import repoutils

# old: svn
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

# git
reponame = "MCViNE"
branch = "master"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
