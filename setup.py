#!/usr/bin/env python

from distutils.core import setup

setup(name='sitemon',
      scripts=['bin/sitemon'],
      version='1.0.0',
      description='A website monitoring program',
      author='Tshaba Phomolo Benedict',
      author_email='benedicttshaba@gmail.com',
      url='http://www.benedict.heliohost.org/',
      packages=['src','src/lib'],
      include_package_data = True,
      license = "GPLv3",
     )
