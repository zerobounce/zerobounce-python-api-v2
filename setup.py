#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

with open('README.md', 'r') as fp:
    README = fp.read()

setup(
    name='zerobounce',
    version='0.1.4',
    description='ZeroBounce Python API - https://www.zerobounce.net.',
    author='Tudor Aursulesei',
    author_email='tudor@zerobounce.net',
    url='http://github.com/zerobounce/zerobounce-python-api',
    long_description=README,
    long_description_content_type="text/markdown",
    download_url'https://github.com/zerobounce/zerobounce-python-api/archive/0.1.4.tar.gz', # I'll explain this in a second
    keywords['email', 'validation'], # arbitrary keywords
    packages=[
        'zerobounce',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
