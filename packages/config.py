name = 'config'
deps = []

from utils.package import repoutils
reponame = 'ctrl'
branch = "config/branches/with_doxygen_and_docbook_support"
repo = repoutils.svn.getPackageRepository(reponame, branch, name=name)
