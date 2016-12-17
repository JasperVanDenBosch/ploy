#!/usr/bin/python
# -*- coding: UTF-8 -*-
from setuptools import setup, find_packages
import os

reqs = [
'mock',
'mako',
'pyramid',
'pyramid_mako',
'pyramid_tm',
'pyramid_zodbconn',
'transaction',
'ZODB3',
'waitress',
'gitpython',
'PyYAML'
]

setup(name='ploy',
      version='0.0',
      author='Jasper J.F. van den Bosch',
      author_email='japsai@gmail.com',
      description='continuous integration',
      packages=find_packages(),
      url = 'https://github.com/ilogue/ploy',
      test_suite="tests",
      scripts=['executables/ploy'],
      zip_safe=False,
      license='BSD',
      long_description='...',
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      install_requires=reqs,
      include_package_data=True,
      entry_points="""\
      [paste.app_factory]
      main = ploy:main
      """,
      )
