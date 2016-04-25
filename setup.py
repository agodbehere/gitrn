#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

requirements = [
    'gitpython',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='gitrn',
    version='0.0.2',
    description="Organize git log and format into release notes",
    long_description=readme,  # + '\n\n' + history,
    author="Andrew B Godbehere",
    author_email='andrew.godbehere@sumupanalytics.com',
    url='https://github.com/agodbehere/gitrn',
    packages=[
        'gitrn',
    ],
    entry_points={
        'console_scripts': [
            'gitrn = gitrn.make_release_notes:run',
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="ISCL",
    zip_safe=True,
    keywords='gitrn',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
