#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This tool helps you to rebase package to the latest version
# Copyright (C) 2013-2014 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# he Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Authors: Petr Hracek <phracek@redhat.com>
#          Tomas Hozza <thozza@redhat.com>

from base.version import VERSION

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='modularity-testing-framework',
    version=VERSION,
    description='Framework for testing modules and containers.',
    keywords='mocules,containers,testing,framework',
    author='Jan Scotka',
    author_email='jscotka@redhat.com',
    url='https://pagure.io/modularity-testing-framework',
    license='GPLv2+',
    packages=['base', 'examples', 'docs'],
    include_package_data=True,
    setup_requires=[],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ]
)
