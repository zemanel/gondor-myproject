gondor-myproject
===============================================================================

About
-----

A kickstart Django 1.3 project setup for <http://gondor.io>, based (but not only) on Gondor.io support docs

Also see <https://github.com/eldarion/gondor-client/tree/feature/startproject/gondor/conf/project_template>

How to use
----------

- Refactor from "myproject" to whatever you like
- Edit myproject/.gondor/config and at least change SECRET_KEY

Django settings
---------------

This project has a "settings.py" mostly based on Django "startproject" defaults, plus custom code to configure **MEDIA_ROOT** and **STATIC_ROOT**.

The WSGI entry point's ("deploy.wsgi") **DJANGO_SETTINGS_MODULE** enviroment variable is configured on "wsgi.py"

[django.contrib.staticfiles](https://docs.djangoproject.com/en/dev/howto/static-files/#using-django-contrib-staticfiles) is enabled by default.

Per-instance settings
---------------------

A "per-instance settings" module exists, for a gondor "**development**" named instance, on **deploy/settings_development.py**

The "per-instance settings module" is imported at the end of gondor's instance **local_settings.py**.

For more information on per-instance settings, read <https://gondor.io/support/quick-how-to/#per-instance-settings>

Media files
-----------

Gondor config is configured to serve static/media files from **/site_media/static/** and **/site_media/media/** respectively.

