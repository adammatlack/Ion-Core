#!/usr/bin/env python2

from distutils.core import setup

setup(name='python-darksilkrpc',
      version='0.1',
      description='Enhanced version of python-jsonrpc for use with DarkSilk',
      long_description=open('README').read(),
      author='Jeff Garzik',
      author_email='<jgarzik@exmulti.com>',
      maintainer='Jeff Garzik',
      maintainer_email='<jgarzik@exmulti.com>',
      url='http://www.github.com/jgarzik/python-darksilkrpc',
      packages=['darksilkrpc'],
      classifiers=['License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)', 'Operating System :: OS Independent'])
