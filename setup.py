# -*- coding: utf-8 -*-
u"""
Setup script
"""
from distutils.core import setup

with open('README.md') as readme:
    long_description = readme.read()

setup(
    name='<your package>',
    version='0.1',
    author='Some author',
    author_email='developer@example.com',
    packages=[],
    license='BSD',
    description='Autopayment Project',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        ],
    )