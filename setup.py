#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()

requirements = []

test_requirements = []

setup(
    name='containers',
    version='0.1.0',
    description='Containers is a python module to easily manipulate app containers.',
    long_description=readme,
    author='Louis Taylor',
    author_email='kragniz@gmail.com',
    url='https://github.com/kragniz/containers',
    packages=[
        'containers',
    ],
    package_dir={'containers':
                 'containers'},
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    keywords='containers appc rocket coreos',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
