

## tree structure of this releaser
##
## This module keeps the information about the tree
## structure of this releaser. 
##
## If source tree changes, only the variable _tree needs
## to be changed.
##


import os
path = os.path.dirname( __file__ )
rootname = os.path.split(path)[-1]

_tree = (
    rootname, "simulation releaser tree", \
    [
     ('src', 'sources', []),
     ('install-deps', 'installation scripts for external dependencies', []),
     ('package', 'packages to be included in this release', []),
     ('paths', 'helpers to figure out paths of external packages?',[]),
     ('utils', 'utilities',[])
    ]
    )
     

from utils.dir_tree import createTree as _createTree, setPaths, printTree


def createTree(  root_path ):
    tree = _createTree( _tree )
    setPaths( tree, root_path )
    return tree


print "-Initializing directory structure representation"
tree = createTree( os.path.dirname(__file__) )

printTree(tree)
