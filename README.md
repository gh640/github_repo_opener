# `github_repo_opener`

A CLI tool to open a front page of owned GitHub repositories quickly.

## Installation

```
$ pip install github_repo_opener
```

## Prerequisition

User has a GitHub access token.

## Usage

Once installed the package, you can use `github-repo-opener` command.

```
$ github-repo-opener
```

### Prepare a local database

```
$ github-repo-opener initdb
```

### Fetch repository data and store them in the local database

```
$ github-repo-opener fetch
```

### Show repository names

```
$ github-repo-opener show
```

### Open a repository front page

```
$ github-repo-opener open
```

### Drop the local database

```
$ github-repo-opener dropdb
```

## License

Licensed under MIT license.
