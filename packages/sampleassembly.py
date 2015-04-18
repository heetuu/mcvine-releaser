from utils.packages.sampleassembly import *

from utils.package import repoutils
# svn
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

# git
reponame = "sampleassembly"
branch = "master"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
