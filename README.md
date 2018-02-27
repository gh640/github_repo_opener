# `github_repo_opener`

A CLI tool to open a front page of owned GitHub repositories quickly.

## Installation

...

## Prerequisition

User has a GitHub access token.

## Usage

Once installed, you can use `github-repo-opener` command.

```bash
$ github-repo-opener
```

### Prepare a local database

```bash
$ github-repo-opener initdb
```

### Fetch repository data and store them in the local database

```bash
$ github-repo-opener fetch
```

### Show repository names

```bash
$ github-repo-opener show
```

### Open a repository front page

```bash
$ github-repo-opener open
```

### Drop the local database

```bash
$ github-repo-opener dropdb
```

## License

Licensed under MIT license.
