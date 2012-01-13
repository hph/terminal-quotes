#!/usr/env python
#coding=utf8

import sys
from platform import system
from os import environ

# NOTE Maybe not the correct format for the variable names, use uppercase?
__author__ = 'Haukur Páll Hallvarðsson'
__author-email__ = 'haukurpallh@gmail.com'
__version__ = '1.0'
__platform__ = system()

def install():
    if __platform__ == 'Linux':
        home_folder = environ['HOME']
    else:
        pass
        # NOTE Add Mac and/or Windows support later.
        # NOTE Finish.
    with open(home_folder, 'a') as bashrc:
        bashrc.write('python %s/termquotes.py' % setup_folder)

def main():
    '''A little error handling. Calls install if the argument "install" is
    passed when run.'''
    if len(sys.argv) == 1:
        print 'Error: No argument passed.'
        if __platform__ in ['Linux', 'Darwin']:
            print 'Type "python setup.py install" to install the program.'
        else:
            # The "python" command is not required or available.
            print 'Type "setup.py install" to install the program.'
    elif sys.argv[1] == 'install':
        install()
    elif sys.argv[1] in ['-v', '--version']:
        print 'Termquotes v%s by %s.' % (__version__, __author__)
        print 'Contact:', __author-email__
    elif sys.argv[1] in ['-h', '--help']:
        print 'Options:'
        print '  -h, --help\t\tshow this message and exit.'
        print '  -v, --version\t\tprint version and exit.'
        print '  install\t\tinstall the program and exit.'
    else:
        print 'Unknown option: %s' % ' '.join(sys.argv[1:])
        if __platform__ in ['Linux', 'Darwin']:
            print 'Type "python setup.py -h for more information.'
        else:
            print 'Type "setup.py -h for more information.'

if __name__ == '__main__':
    main()
