from utils.packages.ins_crystal import *

revision=624

from utils.package import repoutils
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name, revision=revision)
