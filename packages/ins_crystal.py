from utils.packages.ins_crystal import *

revision=624
path, checkoutCmd, updateCmd = repoutils.svn.repoinfo( reponame, branch, name=branch, revision=revision)

