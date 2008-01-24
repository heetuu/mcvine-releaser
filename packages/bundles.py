

#a dictionary of {bundleName: bundleContents}
#a bundle is a collection of packages
bundleInfo = {
    "Prerequisite": [
    'distutils-adpt',
    "config",
    ],
    
    "Pythia": [
    'pythia',
    'pyregui',
    ],

    "basic": [
    'stdVector',
    'array_kluge',
    'histogram',
    ],

    "Nexus": [
    'hdf5fs',
    'nx5',
    ],
    
    "Core": [
    'cctbx_adpt',
    'simulation',
    'mcstas',
    ],

    "Reduction" : [
    'instrument',
    'measurement',
    'reduction',
    #'ins-data',
    ],
    }


#this sequence needs to be maitained so that dependency problem is partially
#solved.
#more basic bundles are in the front.
bundleNames = [
    'Prerequisite',
    'Pythia',
    'basic',
    'Nexus',
    'Core',
    'Reduction',
    ]



