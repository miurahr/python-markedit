#!/usr/bin/env python
import os
from setuptools import setup, find_packages

setup(
    name="python-markedit",
    author="Hiroshi Miura",
    author_email="miurahr@linux.com",
    version='0.1',
    description="markedit library split from symposion",
    url="https://github.com/miurahr/python-markedit/",
    packages=['markedit'],
    include_package_data=True,
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ),
    package_data={'markedit': ['templates/markedit/*.html',
                               'templates/markedit/includes/*.html',
                               'static/js/*.js',
                               'static/js/lang/*.js',
                               'static/css/*.css',
                               'static/css/images/*.[gif|png]'
                               ]}
)
