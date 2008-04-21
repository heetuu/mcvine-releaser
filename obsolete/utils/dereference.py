import os, shutil

def dereference( path ):
    if not os.path.islink(path): return
    rpth = os.path.realpath( path )
    os.remove(path)
    if os.path.isdir( rpth ): 
        shutil.copytree( rpth, path )
    elif os.path.isfile(rpth): 
        shutil.copyfile( rpth, path )
    else: raise IOError
    return


def dereference_recursively( path ):
    print "- dereferencing %s" % path
    dereference( path )
    if not os.path.isdir(path): return
    for item in os.listdir( path ):
        dereference_recursively( os.path.join( path, item ) )
        continue
    return