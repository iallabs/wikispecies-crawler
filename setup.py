# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Licapy',
    version='0.0.1',
    description='',
    long_description=readme,
    author='Imperial Alpha Laboratory',
    author_email='',
    url='',
    license=license,
    packages=find_packages(exclude=('Test', 'Docs'))
)
