# -*- coding: utf-8 -*-

#
# setup.py - Setup script for epanet-toolkit python package
#
# Created:    7/2/2018
# Modified:   2/6/2020
#
# Author:     Michael E. Tryby
#             US EPA - ORD/NRMRL
#
# Suggested Usage:
#   python setup.py build -- -G"Visual Studio 15 2017 Win64" ..
#


from skbuild import setup
#from setuptools import setup


setup(
    name = 'epanet-toolkit',
    version = '0.5.0',

#    description='',
#    long_description='',

    cmake_args = ['-GVisual Studio 14 2015 Win64'],

    package_dir = {'': 'src'},
    packages = ['epanet.output', 'epanet.solver'],

    package_data = {'epanet.output':['*output.*', '*.dylib', '*.dll', '*.so'],
                    'epanet.solver':['*solver.*', '*.dylib', '*.dll', '*.so']},

    zip_safe=False
)