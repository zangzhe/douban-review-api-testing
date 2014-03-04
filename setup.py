#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='douban-review-api-testing',
      version='0.0.1',
      keywords=('Douban', 'OAuth2', 'Douban Review APIs Testing'),
      description='Python scripts for Douban Review APIs Testing',
      author='zangzhe',
      author_email='zang_zhe@163.com',

      packages=find_packages(),
      include_package_data=True,
      platforms='any',
      install_requires=['py-oauth2>=0.0.8', 'six>=1.4.1'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],)
