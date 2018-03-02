from fabric.api import local


CMD_PREFIX = 'pipenv run '


def validate():
    '''Validates files.'''
    _validate_rst()
    _validate_manifest()


def _validate_rst():
    local(CMD_PREFIX + 'rstcheck README.rst')


def _validate_manifest():
    local(CMD_PREFIX + 'check-manifest')


def build():
    '''Builds package.'''
    local(CMD_PREFIX + 'python setup.py sdist bdist_wheel')


def clear_build():
    '''Clears files generated.'''
    local('rm -r dist build github_repo_opener.egg-info')


def upload_to_pypi(env='test'):
    '''Uploads the dist files to pypi.'''
    if env == 'prod':
        local('twine upload dist/*')
    else:
        local('twine upload --repository testpypi dist/*')
