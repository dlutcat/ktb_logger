#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

version = '0.5'

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
      package_dir={'': 'ktb_logger'},
      packages=['ktb_logger'],
)
