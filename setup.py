from setuptools import setup

import github_repo_opener

required = [
    'click',
    'peewee',
    'prompt-toolkit',
    'pygithub',
]

setup(
    name='github_repo_opener',
    version=github_repo_opener.__version__,
    packages=['github_repo_opener'],
    install_requires=required,
    python_requires='>=3.4',
    entry_points={
        'console_scripts': ['github-repo-opener=github_repo_opener:main'],
    },
)
