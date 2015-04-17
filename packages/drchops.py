from utils.packages.drchops import *
from utils.package import repoutils

# overload branch
# old: svn
# branch = "branches/2-alpha"
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)


branch = "2-alpha"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
