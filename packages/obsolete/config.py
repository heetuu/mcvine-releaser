
setupScript = 'setup_config'
path = 'distutils-adpt/caltechbpconfig'
sub_modules = None
deps = ('distutils-adpt',)
checkoutCmd = None # it is checked out when distutils_adpt is checked out
updateCmd = None # it is updated out when distutils_adpt is checked out


def patch( dest ):
    remove_citconfig_cfiles( dest )
    return


def remove_citconfig_cfiles(dest):
    import os
    targets = os.path.join( dest, path, '*', '*.c' )
    os.system( "rm -rf %s" % targets )
    return


