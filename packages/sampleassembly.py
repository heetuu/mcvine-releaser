from utils.packages.sampleassembly import *

from utils.package import repoutils
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
