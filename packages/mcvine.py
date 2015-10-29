from utils.packages.mcvine import *

from utils.package import repoutils

# old: svn
# repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)

# git
reponame = "mcvine"
branch = "master"
server = "https://github.com/mcvine"
repo = repoutils.git.getPackageRepository(reponame, branch, name=name, server=server)
