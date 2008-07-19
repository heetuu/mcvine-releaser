#!/usr/bin/env python

exported_envs_sh = 'envs.sh'
src_dottools = 'dottools'

class Creater:

    def __init__(self, releaser = None, export = 'EXPORT', src = 'src',
                 dotmcvine = '.mcvine' ):
        if releaser is None:
            releaser = os.path.abspath( '.' )

        self.releaser = os.path.abspath( releaser )
        self.export_root = os.path.join( releaser, export )
        self.src_root = os.path.join( releaser, src )
        self.dotmcvine = os.path.join( releaser, dotmcvine )
        return


    def run(self, path):
        contents = self.render_dot_mcvine( )
        open(path, 'w').write( '\n'.join( contents ) )
        return


    def build_software_installation_info_db(self):
        from packages import mcvine
        cmds = [ 
            'cd %s' % os.path.join(
            self.src_root,
            mcvine.path, 'packages', 'softwareinstallationinfodb',
            'softwareinstallationinfodb.dv' ),
            'mm',
            'cd -',
            ]
        cmd = ' && '.join( cmds )
        if (os.system(cmd)): raise "%r failed" % cmd
        return
    

    def create_envs_sh( self ):
        from utils.install import build_envs_sh
        build_envs_sh( self.export_root )
        return os.path.join( self.export_root, 'bin', exported_envs_sh )


    def render_dot_mcvine( self ):
        self.build_software_installation_info_db()
        envs_sh = self.create_envs_sh( )
        dottools = os.path.join( self.src_root, src_dottools )
        contents = [
            'source "%s"' % dottools,
            'source "%s"' % envs_sh,
            'export DV_DIR="%s"' % self.src_root,
            'export MCSTAS_COMPONENT_LIBDIR="%s"' % os.path.join(
            self.src_root, 'MCViNE', 'trunk', 'packages', 'legacycomponents',
            'mcstas2', 'share', 'McStas-Components' ),
            ]

        return contents

import os

def main():
    Creater().run('.mcvine')
    return


if __name__ == '__main__': main()
