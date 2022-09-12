#!/usr/bin/env python

from distutils.core import setup

setup(name='gps-locaton-finder',
      version='1.0',
      description='Application allowing to find GPS coordinates of any address.',
      author='Iaroslav Zelinskyi',
      author_email='zelinskyi.iaroslav@gmail.com',
      packages=['osmx', 'geopandas'],
     )
