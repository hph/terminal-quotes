#!/usr/env python
#coding=utf8

import sys
import os
from platform import system
from shutil import move

AUTHOR = 'Haukur Páll Hallvarðsson'
EMAIL = 'haukurpallh@gmail.com'
VERSION = '1.0'
PLATFORM = system()

def install():
    if PLATFORM == 'Linux':
        # NOTE Add Mac and/or Windows support later.
        try:
            # NOTE All too manual. Find some setup module.
            home_dir = os.environ['HOME']
            setup_dir = '%s/.termquotes' % home_dir
            current_dir = os.path.dirname(sys.argv[0])
            if not os.path.exists(setup_dir):
                os.makedirs(setup_folder)
            move('%s/termquotes.py' % current_dir, setup_dir)
            move('%s/general.txt' % current_dir, setup_dir)
            move('%s/icelandic.txt' % current_dir, setup_dir)
            with open('%s/.bashrc' % home_dir, 'a') as bashrc:
                bashrc.write('python %s/termquotes.py\n' % setup_dir)
            print 'The program was succesfully installed. Reopen the terminal.'
        except:
            # NOTE Write a README.
            print 'Setup failed. Try installing manually (refer to README).'

def main():
    '''A little error handling. Calls install if the argument "install" is
    passed when run.'''
    # NOTE Add an uninstall option.
    if len(sys.argv) == 1:
        print 'Error: No argument passed.'
        if PLATFORM in ['Linux', 'Darwin']:
            print 'Type "python setup.py install" to install the program.'
        else:
            # The "python" command is not required or available.
            print 'Type "setup.py install" to install the program.'
    elif sys.argv[1] == 'install':
        install()
    elif sys.argv[1] in ['-v', '--version']:
        print 'Termquotes v%s by %s.' % (VERSION, AUTHOR)
        print 'Contact:', EMAIL
    elif sys.argv[1] in ['-h', '--help']:
        print 'Options:'
        print '  -h, --help\t\tshow this message and exit.'
        print '  -v, --version\t\tprint version and exit.'
        print '  install\t\tinstall the program and exit.'
    else:
        print 'Unknown option: %s' % ' '.join(sys.argv[1:])
        if PLATFORM in ['Linux', 'Darwin']:
            print 'Type "python setup.py -h for more information.'
        else:
            print 'Type "setup.py -h for more information.'

if __name__ == '__main__':
    main()
