# coding: utf-8

'''A script to open a front page of owned github repos.
'''

import os
from pathlib import Path
import subprocess
import sys

import click
from github import Github
import peewee as pw
from prompt_toolkit import prompt
from prompt_toolkit.contrib.completers import WordCompleter
from prompt_toolkit.validation import Validator, ValidationError


__version__ = '0.1.0'


GITHUB_TOKEN_KYE = 'GITHUB_ACCESS_TOKEN'
CACHE_PATH = Path.home() / '.cache/github_repo_opener/cache.sqlite3'
CMD_OPEN = {
    'darwin': 'open',
    'win32': 'start',
}


db = pw.SqliteDatabase(str(CACHE_PATH.absolute()))


@click.group()
def main():
    validate_platform()


@main.command()
def initdb():
    m = CacheManager()
    m.create_db()
    m.create_table()
    click.echo('Initialized cache database "{}".'.format(CACHE_PATH))


@main.command()
def dropdb():
    try:
        m = CacheManager()
        m.drop_table()
        m.drop_db()
        click.echo('Dropped cache database "{}".'.format(CACHE_PATH))
    except pw.OperationalError as e:
        sys.exit('Could not find the database.')


@main.command()
def fetch():
    token = get_github_token_or_show_prompt()
    repos = fetch_repo_data(token)
    m = CacheManager()
    count = 0
    try:
        for repo in repos:
            try:
                m.add({
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'html_url': repo.html_url,
                })
                count += 1
            except pw.IntegrityError as e:
                click.echo('Skipped duplicate repo "{}".'.format(repo.name))
        click.echo('Fetched the data of {} repos.'.format(count))
    except pw.OperationalError as e:
        db.close()
        sys.exit('Cannot open database file "{}".'.format(CACHE_PATH))


@main.command()
def show():
    try:
        repos = {repo.name: repo for repo in CacheManager().get_all()}
        click.echo('Total {} repo data found.'.format(len(repos)))
        for repo_name, repo in repos.items():
            click.echo('{}'.format(repo_name))
    except pw.OperationalError as e:
        db.close()
        sys.exit('Cannot open database file "{}".'.format(CACHE_PATH))


@main.command()
def open():
    try:
        repos = {repo.name: repo for repo in CacheManager().get_all()}
        click.echo('Total {} repo data found.'.format(len(repos)))
        repo_name = show_repos_prompt(repos.keys())
        open_repo(repos[repo_name].html_url)
    except pw.OperationalError as e:
        db.close()
        sys.exit('Cannot open database file "{}".'.format(CACHE_PATH))


def validate_platform():
    supported_platforms = CMD_OPEN.keys()
    if sys.platform not in supported_platforms:
        sys.exit(
            'This platform is not supported. '
            'Only the followings are supported: {}.'.format(
                ', '.join(supported_platforms)
            )
        )


def get_github_token_or_show_prompt() -> str:
    if GITHUB_TOKEN_KYE in os.environ:
        print('The access token found in {}'.format(GITHUB_TOKEN_KYE))
        return os.environ[GITHUB_TOKEN_KYE]

    github_access_token = prompt(
        'GitHub access token '
        '(you can set it with {} instead): '.format(GITHUB_TOKEN_KYE),
    )

    return github_access_token


def fetch_repo_data(access_token: str):
    print('Fetching repo names...')
    g = Github(access_token)
    user = g.get_user()
    return [repo for repo in user.get_repos() if repo.owner.id == user.id]


def show_repos_prompt(repo_names) -> str:
    repo_name = prompt(
        'repo name: ',
        completer=WordCompleter(repo_names),
        validator=RepoNameValidator(repo_names),
    )

    return repo_name


def open_repo(repo_url: str):
    cmd = CMD_OPEN[sys.platform]
    subprocess.run([cmd, repo_url])


class RepoNameValidator(Validator):
    def __init__(self, valid_names):
        self._valid_names = valid_names
    def validate(self, document):
        text = document.text

        if text not in self._valid_names:
            raise ValidationError(
                message='Repo name is invalid.',
                cursor_position=len(text),
            )


class BaseModel(pw.Model):
    class Meta:
        database = db


class RepoModel(BaseModel):
    name = pw.CharField(unique=True)
    full_name = pw.CharField()
    html_url = pw.CharField()


class CacheManager:
    def create_db(self):
        parent = CACHE_PATH.parent
        if not parent.is_dir():
            parent.mkdir(parents=True)
        db.connect()
        db.close()

    def drop_db(self):
        db.close()
        CACHE_PATH.unlink()
        parent = CACHE_PATH.parent
        parent.rmdir()

    def create_table(self):
        db.connect()
        db.create_tables([RepoModel])
        db.close()

    def drop_table(self):
        db.connect()
        db.drop_tables([RepoModel])
        db.close()

    def add(self, repo: dict):
        repo = RepoModel(**repo)
        repo.save()

    def get_all(self):
        return RepoModel.select()

    def delete(self, name: str):
        repo = RepoModel.select().where(RepoModel.name == name)
        repo.delete_instance()
