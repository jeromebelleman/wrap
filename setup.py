#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='wrap',
    version='1.0',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Format paragraphs",
    long_description="Format paragraphs by wrapping lines",
    scripts=['wrap'],
    data_files=[],
)
