# coding: utf-8

'''A script to open a front page of owned github repos.
'''

import os
import subprocess

from github import Github
import inquirer


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

    questions = [
        inquirer.Password(
            'github_access_token',
            message='GitHub access token',
            validate=lambda _, x: x
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers['github_access_token']


def get_repos(access_token: str) -> dict:
    print('Fetching repo names...')
    g = Github(access_token)
    return {repo.name: repo.full_name for repo in g.get_user().get_repos()}


def show_repos_prompt(repo_names) -> dict:
    questions = [
        inquirer.List(
            'repo_name',
            message='Select the repo to open',
            choices=repo_names,
            carousel=True,
        ),
    ]

    answers = inquirer.prompt(questions)
    return answers['repo_name']


def open_repo(full_name: str):
    repo_url = URL.format(path=full_name)
    subprocess.run(['open', repo_url])


if __name__ == '__main__':
    main()
