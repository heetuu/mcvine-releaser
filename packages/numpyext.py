from utils.packages.numpyext import *

from utils.package import repoutils

repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
