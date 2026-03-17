#!/usr/bin/env python

from setuptools import setup


setup(
    name='pyhocon',
    version='0.3.61',
    description='HOCON parser for Python',
    long_description='pyhocon is a HOCON parser for Python. Additionally we provide a tool (pyhocon) to convert any HOCON '
                     'content into json, yaml and properties format.',
    keywords='hocon parser',
    license='Apache License 2.0',
    author='Francois Dang Ngoc',
    author_email='francois.dangngoc@gmail.com',
    url='http://github.com/chimpler/pyhocon/',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    python_requires='>=3.10',
    packages=[
        'pyhocon',
    ],
    install_requires=[
        'pyparsing>=3,<4',
    ],
    extras_require={
        'Duration': ['python-dateutil>=2.8.0'],
        'test': ['pytest']
    },
    entry_points={
        'console_scripts': [
            'pyhocon=pyhocon.tool:main'
        ]
    },
)
