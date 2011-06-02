gondor-myproject
================

About
-----

A blank django 1.3 project setup for <http://gondor.io>, based (but not only) on Gondor.io support docs

How to use
----------

- Refactor from "myproject" to whatever you like
- Edit myproject/.gondor/config

Django settings
---------------

- Sample settings profiles have been separated in the 'settings' module, that import "settings.common" as a base
- Gondor wsgi configuration uses 'settings.production' module by default, which imports gondor's "local_settings.py"
- Gondor's "local_settings.py" overrides MEDIA_ROOT and STATIC_ROOT, but a sample configuration exists for local development

