#!/opt/python3.7/bin/python

from setuptools import setup

setup(
    name = 'pycli',
    version = '0.0.1',
    packages = ['pycli'],
    entry_points = {
        'console_scripts' : [
            'pycli = pycli.__main__:main'
        ]
    }
)