#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='online-judge-verify-helper',
    version='0.1.0',
    author='Kimiyuki Onaka',
    author_email='kimiyuki95@gmail.com',
    url='https://github.com/kmyk/online-judge-verify-helper',
    license='MIT License',
    description='',
    install_requires=[
        'online-judge-tools == 7.*',
    ],
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points={
        'console_scripts': [
            'oj-verify = onlinejudge_verify.main:main',
        ],
    },
)
