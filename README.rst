znbpost
=====================================================

Django application to manage articles, pages and similar content.

Features
------------------------------------------------------------------------------

- Provides a base model to create articles and pages from.

Installing and Uninstalling Packages
------------------------------------------------------------------------------

Installing in editable mode from local directory.

.. code-block:: bash

  $ pip install -e /path/to/znbpost/

You can remove the -e to install the package in the corresponding Python path, for example: /env/lib/python3.7/site-packages/znbpost.

List installed packages and uninstall.

.. code-block:: bash

  $ pip list
  $ pip uninstall znbpost

Installing from git using https.

.. code-block:: bash

  $ pip install git+https://github.com/requests/requests.git#egg=requests
  $ pip install git+https://github.com/alexisbellido/znbpost.git#egg=znbpost

This package could be added to a pip requirements.txt file from its git repository or source directory.

.. code-block:: bash

  git+https://github.com/alexisbellido/znbpost.git#egg=znbpost
  -e /path-to/znbpost/

or from PyPi, in this case passing a specific version.

.. code-block:: bash

  znbpost==0.2

Installing znbpost will require the necessary packages.
