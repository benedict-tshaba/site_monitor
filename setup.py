#!/usr/bin/env python

from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(name='sitemon',
      scripts=['bin/sitemon'],
      version='1.0.3',
      description='A website monitoring program',
      long_description=readme,
      author='Tshaba Phomolo Benedict',
      author_email='benedicttshaba@gmail.com',
      url='http://www.benedict.heliohost.org/',
      packages=['src','src/lib'],
      include_package_data = True,
      license = license,
     )
