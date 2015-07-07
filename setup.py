#!/usr/bin/env python
from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session = False)
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="markedit",
    author="Hiroshi Miura",
    author_email="miurahr@linux.com",
    version='0.2.dev4',
    description="markedit library for django integration",
    url="https://github.com/miurahr/python-markedit/",
    packages=['markedit'],
    install_requires = reqs,
    include_package_data=True,
    classifiers=(
        "Development Status :: 3 - Alpha",
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
                               'static/markedit/*.js',
                               'static/markedit/lang/*.js',
                               'static/markedit/*.css',
                               'static/markedit/images/*.[gif|png]'
                               ]}
)
