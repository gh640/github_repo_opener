import codecs
import os

from setuptools import setup

import github_repo_opener

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

required = [
    'click',
    'peewee',
    'prompt-toolkit',
    'pygithub',
]

setup(
    name='github_repo_opener',
    version=github_repo_opener.__version__,
    description='A tool to open your GitHub repository page quickly.',
    long_description=long_description,
    url='https://github.com/gh640/github_repo_opener',
    author='Goto Hayato',
    author_email='habita.gh@gmail.com',
    keywords='github',
    packages=['github_repo_opener'],
    install_requires=required,
    python_requires='>=3.4',
    entry_points={
        'console_scripts': ['github-repo-opener=github_repo_opener:main'],
    },
    license='MIT',
)
