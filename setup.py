''' 
               setup.py

               ver 0.2
          author : Yasutaka Nishida
          date   : 2020/12/11               
                                           '''

#coding:utf-8

#from setuptools import setup, find_packages
from distutils.core import setup
from codecs import open
from os import path
import re

root_dir = path.abspath(path.dirname(__file__))

setup(
    name='strayqat',
    version='0.2',
    description='A topological data analysis toolkit for material science',
    long_description='README.txt',
    author='Yasutaka Nishida',
    author_email='yasutaka.nishida@toshiba.co.jp',
    install_requires=[
        'pyscf', 'openfermion', 'openfermionpyscf', 'scipy==1.4.1', 'qulacs'
    ],
    license='LICENSE.txt',
    packages=['strayqat', 'strayqat.src'],
    package_dir={'strayqat': 'strayqat'},
)
