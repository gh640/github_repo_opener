import codecs
import os
from pathlib import Path

from setuptools import setup

# here = os.path.abspath(os.path.dirname(__file__))
here = Path(__file__).parent

with codecs.open(here / 'README.rst', encoding='utf-8') as f:
    long_description = '\n' + f.read()

required = ['click>=6.0', 'peewee>=3.0.0', 'prompt-toolkit', 'pygithub>=1.0']


about = {}
with open(here / 'github_repo_opener/__version__.py', 'r', encoding='utf-8') as f:
    exec(f.read(), about)

setup(
    name='github_repo_opener',
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    url='https://github.com/gh640/github_repo_opener',
    author=about['__author__'],
    author_email=about['__author_email__'],
    keywords='github repository',
    packages=['github_repo_opener'],
    install_requires=required,
    python_requires='>=3.4',
    entry_points={'console_scripts': ['github-repo-opener=github_repo_opener:main']},
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
        'Topic :: Software Development :: Version Control :: Git',
        'Topic :: Utilities',
    ],
)
