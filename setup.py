from setuptools import setup, find_packages
from os.path import join, dirname

import lumbda

setup(
    name='lumbda',
    version=lumbda.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author=lumbda.__author__,
    author_email=lumbda.__author_email__,
    url='https://github.com/lumapps/lumbda',
    license=open(join(dirname(__file__), 'LICENSE')).read(),
    keywords=['utilities', 'utils'],
    install_requires=[],
)
