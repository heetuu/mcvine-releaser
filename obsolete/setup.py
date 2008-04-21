#!/usr/bin/env python

###############################################################################
#For release developer:
#This is the main setup script.
#Only "main" method needs to be redefined when creating release for a
#new software.
###############################################################################

# bundle > package > module


#all sources are under directory 'src'
srcRoot = 'src'

#put distutils_adpt to the python path. this is essential because all setup
#scripts rely on distutils_adpt
import sys, os
# here we assume that the package distutils_adpt is in the current directory
sys.path = [os.path.join( os.getcwd(), srcRoot, 'distutils-adpt')]  + sys.path


from packages import *
from deps import *


def importSetupScript( name ):
    """import the setup script of the given package

    -name:  the name of the package
    
    return a tuple of (module, source directory, saved sys.path )
    """
    #get to know more about this package
    info = packageInfoTable[name]
    setupScriptName, sourceDir, all_sub_modules= \
                     info['setupScript'], info['path'], info['sub_modules']
    import sys,os
    save = sys.path
    cwd = os.getcwd()
    sys.path = [ os.path.join( cwd, srcRoot, sourceDir) ] + sys.path
    setupScript = __import__( setupScriptName )
    return setupScript, setupScriptName, sourceDir, save


def getDefaultModules( name ):
    """retrieve the default modules to be installed for a given package

    - name: the name of the package
    """
    #import setup script
    setupScript, setupScriptName, sourceDir, save = importSetupScript( name )
    #get default modules
    modules = setupScript.__dict__.get("defaultModules")
    #restore sys.path to avoid potential conflicts among packages
    sys.path = save
    return modules


def add( name, modules, software):
    "add package with name and packageInfo to the whole software"
    #import setup script
    setupScript, setupScriptName, sourceDir, save = importSetupScript( name )
    #retrieve "preparePackage" from the setup script
    preparePackage = setupScript.preparePackage
    #need to be careful with packages with sub modules
    import os
    sourceDir = os.path.join( srcRoot, sourceDir )
    if modules: preparePackage( software, sourceDir, modules )
    else: preparePackage( software, sourceDir )
    #restore
    sys.path = save
    return


def setupIndividually( name, modules ):
    """setup a package

    - name:    name of the package
    - modules: sub modules inside the package
    """
    #import setup script
    setupScript, setupScriptName, sourceDir, save = importSetupScript( name )
    #initialize package to be installed
    from distutils_adpt.Package import Package
    package = Package( name, "" )

    #modules inside a package
    if modules is None:
        #if user said nothing, we should come up with a default
        modules = setupScript.__dict__.get("defaultModules")
        pass
    #
    if not modules:
        #no modules
        setupScript.preparePackage(package, sourceDir)
    else:
        #yes.
        setupScript.preparePackage(package, sourceDir, modules=modules)
        pass
    
    #setup
    try:
        #try to setup package
        package.setup()
    except SystemExit , msg:
        #if error, try to print out a nice error message

        #figure out the paths of which packages are needed
        paths_requirements = []
        from distutils_adpt.paths.Paths import Paths
        for pathkey in Paths.__its__.keys():
            if setupScriptName in Paths(pathkey).visitors:
                paths_requirements.append( pathkey )
                pass
            continue
        
        nmsg = "The following packages are required for a successful installation of %s:\n" % name
        nmsg += str( paths_requirements ) + '\n'
        nmsg += "\n"
        from operator import add
        nmsg += reduce( add, [str(Paths(pathkey))+'\n' for pathkey in paths_requirements ], "")
        nmsg += "\n" + '*'*70 + '\n' + str(msg) +'\n'+ '*'*70 
        raise SystemExit(nmsg)
            
    #restore
    #os.chdir( cwd )
    sys.path = save
    if modules!= None: return {name: modules}
    else:              return {name: "All"}



def parseOptions( argv, keywords ):
    """get values for input keywords

    inputs like:
    --keyword=value

    transformed to a dictionary of 
    {keyword: value}

    if nothing is given, value is set to default: True
    """
    res = {}
    for keyword in keywords:
        for i, item in enumerate(argv):
            if item.startswith(keyword):
                value = item[ len(keyword) + 1: ]
                if value == "": value = True
                res[keyword] = value
                del argv[i]
                pass
            continue
        continue
    return res


def getBundleContent(name):
    "get the names of the packages included in a bundle, given the bundle name"
    if name in bundleInfo.keys():
        return bundleInfo[name]
    else:
        raise "No such bundle: %s" % name
    raise


def sortPackages( packages ):
    "sort packages so more basic packages are built earlier"
    # this is to ensure the correct sequence of building
    sum = []
    for packageName in packageSequence:
        if packageName in packages: sum.append( packageName )
        continue
    return sum
        
    

def addBundleToPackages(name, packages):
    """
    this function add all packages in the given bundle to the list "packages"
    
    - packages:    a list of packages
    - name:        the name of a bundle.
    """
    for package in getBundleContent(name):
        if not (package in packages):
            packages.append(package)
            pass
        continue
    return packages


def sum_of_Bundles_and_Packages(names, packages):
    """
    this function add all packages included in each bundle to the list "packages".
    names:      a list of bundle names.
    packages:   a list of package names.
    """
    if not names is None and packages is None: packages = []
    for name in names: addBundleToPackages( name, packages )
    return packages

        

def yes( answer ):
    "test if the answer is yes"
    if answer == None: return False #no answer, so we don't think it is a yes
    if answer == True : return True #sure
    if isinstance( answer, str ):
        if answer.lower() == 'y' or answer.lower() == 'yes': return True #sure
        if answer.lower() == 'n' or answer.lower() == 'no':  return False #sure
        pass
    #raise ValueError, "Unrecognized answer %s. Please say yes or no" % answer
    raise ValueError, "Unrecognized answer %s. Please check your syntax" % answer



def parseCommandLine():
    "parse command line options"
    #this function now becomes very complex. please run tests at the
    #end of this script if you revise this function
    import sys, getopt
    argv = sys.argv

    keywords = ['--bundles', '--packages']
    keywords += ['--with-%s'%package for package in packageNames]
    keywords += ['--with-%s'%bundle  for bundle  in bundleNames ]
    keywords += ['--without-%s'%package for package in packageNames]
    keywords += ['--without-%s'%bundle  for bundle  in bundleNames ]
    options = parseOptions( argv, keywords )


    bundles = packages = None
    if options.get('--bundles'): bundles = options['--bundles'].split(',')
    if options.get('--packages'): packages = options['--packages'].split(',')


    if bundles and 'all' in bundles: bundles = bundleNames[:]
    if packages and 'all' in packages: packages = packageNames[:]


    #combine bundles and packages, so we have a list of packages to install
    if bundles != None:
        #if bundles are given then we need a sum of bundles and packages
        packages = sum_of_Bundles_and_Packages( bundles, packages )
    elif packages == None:
        #if no bundles and no packages are supplied
        #we need a default list of packages
        packages = defaultPackages
        pass
    else:
        #otherwise, we must have packages that is not empty. that is good
        pass


    #if user supply inputs to keywords like --with-<package name>
    #we shoudl deal with it here
    bundles = None
    for bundle in bundleNames:
        #check sanity
        with_bundle = yes( options.get('--with-%s'%bundle) )
        without_bundle = yes( options.get('--without-%s'%bundle) )
        if with_bundle and without_bundle:
            msg = "@#$%^&*@#$"*5, '\n'
            msg += "Hey, you want to confuse me? You are really good on that."
            msg += "Let me know your real decision: with or without %s" % bundle
            raise Exception, msg
        #with
        if with_bundle:
            if bundles == None: bundles = [bundle]; continue
            if not bundle in bundles: bundles.append(bundle); continue
            continue
        #without
        if without_bundle:
            for p in bundleInfo[bundle]:
                if p in packages:
                    del packages[packages.index(p)]
                continue
            continue
        continue
    if bundles!=None: packages = sum_of_Bundles_and_Packages( bundles, packages )
    
    for package in packageNames:
        with_package = yes( options.get('--with-%s'%package) )
        without_package = yes( options.get('--without-%s'%package) )
        if with_package and without_package:
            msg = "@#$%^&*@#$"*5 + '\n'
            msg += "Hey, you want to confuse me? You are really good at that. "
            msg += "Let me know your real decision: with or without %s" % package
            raise Exception, msg

        if with_package:
            if packages == None: packages = [package]; continue
            elif not package in packages: packages.append(package); continue
            continue

        if without_package:
            if package in packages: del packages[packages.index(package)]; continue
        continue

    print '='*70
    print ' '*2, "Packages requested are"
    print ' '*4, packages
    print '='*70

    #check dependency
    checkDependencies(packages, modules)

    #distutils_adpt should be put in, because dependency checks will always fail
    #to notice that distutils_adpt may not have been installed. The reason is that
    #distutils_adpt directory is included in python path at the beginning of
    #this script so the distutils_adpt package will always pass the "import test"
    #used by function checkDependencies to test if a package has been installed.
    packages.append( "distutils_adpt" )
    

    #sort the installation list so that we have more basic packages installed earlier
    packages = sortPackages(packages)
    

    print '='*70
    print ' '*2, "Packages to be installed are"
    print ' '*4, packages
    print '='*70
    return packages, modules
        
    
    


class DependencyError(Exception): pass


def checkDependencies( packages, modules ):
    """check dependencies of packages

    packages: a list of packages that are going to be installed
    modules:  a dictionary. modules[package] are submodules inside package that are chosen to be installed
    """
    #save the package length, so that after this dependency check, we can know
    #if more pakcages are added into the install list. If some more packages were
    #added into the installation list, we need to run dependency check list again.
    nPackages = len(packages)
    
    print "\n-> checking dependencies ..."
    import sys
    save = sys.path
    #loop over all packages
    for package in packages:
        print "\n--> check dependencies of package %r" % package
        #sub modules of package
        sub_modules = modules.get(package)
        #if no modules is given from user input. default modules will be used
        defaultModules = getDefaultModules(package)
        if sub_modules is None: sub_modules = defaultModules
        #check dependencies of the package with chosen sub modules
        _check_dependencies( package, sub_modules, packages)
        continue
    #restore python path
    sys.path = save

    #
    if len(packages)>nPackages: checkDependencies( packages, modules )
    return


def _check_dependencies( package, sub_modules, install_packages):
    """check dependecies of a package with chosen sub_modules
    """
    info = packageInfoTable[package]
    sourceDir, prerequisites = info['path'], info['deps']
    if sub_modules:
        for module in sub_modules:
            _check_depends( module, prerequisites[module], install_packages )
            continue
        pass
    else:
        _check_depends( package, prerequisites, install_packages )
        pass
    return


def _check_depends( package, prerequisites, install_packages ):
    """check each package inside prerequisites.
    it must be either inside the  install_packages, or already installed"""
    for item in prerequisites:
        if item in install_packages:
            #good. it is going to be installed
            print "---> Good. %s is going to be installed" % item
            continue 
        #if not. try to see if it is already installed
        try:
            print "---> try import %s ..." % item ,
            m = __import__( item )
            print " %s found" % m

        except ImportError :
            if item in packageNames:
                #that means we could just add this new item to installation list
                print "Add %s to installation list" % item
                install_packages.append( item )
            else:
                msg = '\n'
                msg += 70*'*'+'\n'
                msg += "To install %s, you must first install all the following packages:\n %s.\n\n" % (
                    package, prerequisites)
                msg += "Currently, at least %r is missing.\n\n" % item
                msg += "%s: %s" % (item, externPackageInfo[item])
                msg += '\n' + 70*'*'
                raise DependencyError, msg
            pass
        continue
    return


def testOptionParser( options, expected = None):
    print "--> testing command line options %s " % options
    import sys
    sys.argv = options
    packages, modules = parseCommandLine()
    print
    if expected is None: return
    msg = "packages(%s) != expected(%s)" % (packages, expected)
    for item in expected:
        if not item in packages:
            raise msg
    for item in packages:
        if not item in expected:
            raise msg
    return

    
def testCommandLineParsing():
    testOptionParser( ['build', '--bundles=Pythia'],
                      expected = ['distutils_adpt'] + bundleInfo['Pythia'] )
    testOptionParser( ['build'],
                      expected = defaultPackages )
    testOptionParser( ['build', '--with-pyre'],
                      expected = defaultPackages)
    testOptionParser( ['build', '--with-Pythia'],
                      expected = defaultPackages )
    testOptionParser( ['build', '--with-Simulation'],
                      expected = defaultPackages+bundleInfo['Simulation'] )
    testOptionParser( ['build', '--bundles=Pythia', '--with-pyre'],
                      expected = ['distutils_adpt'] + bundleInfo['Pythia'] )
    testOptionParser( ['build', '--bundles=Pythia', '--with-Simulation'],
                      expected = ['distutils_adpt'] + bundleInfo['Pythia'] + bundleInfo['Simulation'] )
    tmp = defaultPackages[:]; del tmp[tmp.index('pyre')]
    testOptionParser( ['build', '--without-pyre'],
                      expected = tmp)
    
    tmp = defaultPackages[:]
    for a in bundleInfo['Pythia']:
        if a in tmp: del tmp[tmp.index(a)]
    testOptionParser( ['build', '--without-Pythia'],
                      expected = tmp)
    
    tmp = bundleInfo['Pythia'][:]; del tmp[tmp.index('pyre')]
    testOptionParser( ['build', '--bundles=Pythia', '--without-pyre'])
    
    testOptionParser( ['build', '--bundles=Pythia', '--without-Simulation'],
                      expected = ['distutils_adpt'] + bundleInfo['Pythia'])
    
    testOptionParser( ['build', '--bundles=all'],
                      expected = packageNames)
    testOptionParser( ['build', '--packages=all'],
                      expected = packageNames)
    return


def tests():
    testCommandLineParsing()
    return


def setupAll(packages, modules):
    #run thru all packages and setup them individually
    installed = {}
    for package in packages:
        if package in packageInfoTable.keys():
            print "--> setup %s " % package
            installed.update( setup( package, modules = modules.get(package) ) )
            pass
        else:
            print '*'*70
            print '  Don\'t know anything about %s' % package
            print '  ignored'
            print '*'*70
            pass
        continue
    return installed


def addAll(packages, modules, software):
    """
    run thru all packages and add them into the top-level package
    """
    for package in packages:
        if package in packageInfoTable.keys():
            print "--> add %s to %s" % (package, software.name)
            add( package, modules.get(package), software ) 
            pass
        else:
            print '*'*70
            print '  Don\'t know anything about %s' % package
            print '  ignored'
            print '*'*70
            pass
        continue
    return


def printReport(installed):
    print
    print "*"*70
    print "  Packages included in this release are:"
    print "   ", packageNames
    print
    print " ", "-"*66
    print
    print "  Following packages have been installed"
    packages, modules = installed
    for package in packages:
        _modules = modules[package]
        if _modules is None: _modules = "All"
        print "    %s: %s" % (package, _modules)
    print "*"*70
    return


def _write_scheme():
    # load scheme from pickle file
    # see distutils_adpt.install
    import pickle
    scheme = pickle.load( open( "scheme.pkl" ) )
    from write_scheme import write_scheme
    write_scheme( scheme )
    return
    


def main():
    import os
    curdir = os.path.abspath( os.curdir )
    
    #parse user inputs
    packages, modules = parseCommandLine()

    #create the package
    from distutils_adpt.Package import Package

    from release import name, version
    release = Package(name, version)

    #setup 
    # installed = setupAll( package, modules )  #-- setup individually
    addAll( packages, modules, release )  # add everything into the top-level package


    # setup
    release.setup()
    installed = packages, modules

    # report printing
    printReport( installed )

    # write scheme if install
    try: _write_scheme()
    except: pass
    
    return
    


if __name__ == "__main__":
    #tests()
    main()


#tests
"""
$ ./setup.py install --prefix=$PREFIX 


$ ./setup.py install --prefix=$PREFIX --packages=all


$ ./setup.py install --prefix=$PREFIX --bundles=Pythia,Reduction


$ ./setup.py install --prefix=$PREFIX --bundles=Pythia --packages=stdVector


$ ./setup.py install --prefix=$PREFIX --packages=all --without-reduction
"""
