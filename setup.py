#!/usr/bin/env python

from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
    packages=['rqt_graph'],
    package_dir={'': 'src'},
    scripts=['scripts/rqt_graph']
)

setup(**d)
