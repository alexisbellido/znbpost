Setting up ZnbPost
==================================================================================

Once you have a container running with a Django project you can install the znbpost package, if you haven't done so already

.. code-block:: bash

  $ pip install -e /root/znbpost/
  
Then add the application (znbpost.apps.ZnbPostConfig) to your Django settings.py, ssh into a container running the Django project and activate the models.
  
.. code-block:: bash

  $ django-admin makemigrations znbpost
  $ django-admin sqlmigrate znbpost 0001 # optional to print SQL
  $ django-admin migrate
  

