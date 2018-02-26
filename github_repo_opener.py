# coding: utf-8

'''A script to open a front page of owned github repos.
'''

import os
import subprocess

from github import Github
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError


GITHUB_TOKEN_KYE = 'GITHUB_ACCESS_TOKEN'
URL = 'https://github.com/{path}'


def main():
    token = get_github_token_or_show_prompt()

    repos = get_repos(token)
    repo_name = show_repos_prompt(repos.keys())

    open_repo(repos[repo_name])


def get_github_token_or_show_prompt() -> str:
    if GITHUB_TOKEN_KYE in os.environ:
        print('The access token found in {}'.format(GITHUB_TOKEN_KYE))
        return os.environ[GITHUB_TOKEN_KYE]

    github_access_token = prompt('GitHub access token: ')

    return github_access_token


def get_repos(access_token: str) -> dict:
    print('Fetching repo names...')
    g = Github(access_token)
    return {repo.name: repo.full_name for repo in g.get_user().get_repos()}


def show_repos_prompt(repo_names) -> str:
    repo_name = prompt(
        'repo name: ',
        completer=WordCompleter(repo_names),
        validator=RepoNameValidator(),
    )

    return repo_name


def open_repo(full_name: str):
    repo_url = URL.format(path=full_name)
    subprocess.run(['open', repo_url])


class RepoNameValidator(Validator):
    def validate(self, document):
        text = document.text

        raise ValidationError(
            message='Repo name is invalid.',
            cursor_position=len(text),
        )


if __name__ == '__main__':
    main()
