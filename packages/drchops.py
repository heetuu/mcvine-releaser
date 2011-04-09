from utils.packages.drchops import *

# overload branch
branch = "branches/2-alpha"

from utils.package import repoutils
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
