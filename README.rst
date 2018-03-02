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

Prepare a local database
========================

.. code-block:: bash

    $ github-repo-opener initdb

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

Drop the local database
=======================

.. code-block:: bash

    $ github-repo-opener dropdb


*******
License
*******

Licensed under MIT license.
