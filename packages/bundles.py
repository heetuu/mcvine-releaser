

#a dictionary of {bundleName: bundleContents}
#a bundle is a collection of packages
bundleInfo = {
    "Prerequisite": [
    "config",
    ],
    
    "Pythia": [
    'pythia',
    # 'pyregui',
    ],

    "basic": [
    'dsm',
    'numpyext',
    'bpext',
    # 'luban',
    'histogram',
    'ins_matter',
    ],

    "kernel-deps": [
    # 'sansmodels',  # optional
    ],

    "Core": [
    'instrument',
    'sampleassembly',
    'mcvine',
    ],

    "reduction": [
    'drchops',
    ],

    }


#this sequence needs to be maitained so that dependency problem is partially
#solved.
#more basic bundles are in the front.
bundleNames = [
    'Prerequisite',
    'Pythia',
    'basic',
    'reduction',
    'Core',
    'kernel-deps',
    ]



