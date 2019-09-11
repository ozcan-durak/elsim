# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='elsim',
    version='0.1.0',
    description='Election simulation and analysis',
    long_description=readme,
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',

        # Social choice theory
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Sociology',

        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='elections voting social choice theory',
    author_email='endolith@gmail.com',
    url='https://github.com/endolith/elsim',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'examples')),
    install_requires=[
        'numpy',
    ],
    tests_require=[
        'pytest',
        'hypothesis',
    ],
    extras_require={
        'fast':  ['numba'],
    }
)
