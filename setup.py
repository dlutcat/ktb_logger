#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload -r internal')
    sys.exit()

version = '0.6'

setup(name='ktb_logger',
      version=version,
      description=u"日志控制模块",
      long_description=open("README.md").read(),
      classifiers=[
        "Programming Language :: Python",
      ],
      author='Pat',
      author_email='pat.inside@gmail.com',
      zip_safe=False,
      install_requires=[
          'setuptools',
          'gevent',
      ],
      tests_require=[
          'nose',
      ],
      test_suite='nose.collector',
      packages=['ktb_logger'],
)
