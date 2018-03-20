####################
`github_repo_opener`
####################

A CLI tool to open a front page of owned GitHub repositories quickly.


************
Installation
************

.. code-block:: bash

    $ pip install github_repo_opener


**************
Prerequisition
**************

User has a GitHub access token.


*****
Usage
*****

Once installed the package, you can use `github-repo-opener` command.

.. code-block:: bash

    $ github-repo-opener

.. image:: https://raw.githubusercontent.com/gh640/github_repo_opener/master/assets/capture-01-no-command.gif

Prepare a local database
========================

.. code-block:: bash

    $ github-repo-opener initdb

This creates a sqlite database file at :code:`~/.cache/github_repo_opener/cache.sqlite3`.

Fetch repository data and store them in the local database
==========================================================

.. code-block:: bash

    $ github-repo-opener fetch

Show repository names
=====================

.. code-block:: bash

    $ github-repo-opener show

Open a repository front page
============================

.. code-block:: bash

    $ github-repo-opener open

.. image:: https://raw.githubusercontent.com/gh640/github_repo_opener/master/assets/capture-02-open.gif

Drop the local database
=======================

.. code-block:: bash

    $ github-repo-opener dropdb

This deletes the sqlite database file at :code:`~/.cache/github_repo_opener/cache.sqlite3`.


*******
License
*******

Licensed under MIT license.
