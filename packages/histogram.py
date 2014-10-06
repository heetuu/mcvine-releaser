from utils.packages.histogram import *
deps = () # histogram only depends on numpy now

from utils.package import repoutils
repo = repoutils.git.getPackageRepository(reponame, branch, name=name)
