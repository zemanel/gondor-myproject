gondor-myproject
================

About
-----

A blank django 1.3 project setup for <http://gondor.io>, based (but not only) on Gondor.io support docs

Also see <https://github.com/eldarion/gondor-client/tree/feature%2Fstartproject/gondor/conf/project_template>

How to use
----------

- Refactor from "myproject" to whatever you like
- Edit myproject/.gondor/config
- Change SECRET_KEY

Django settings
---------------

- "settings.py" affects Gondor's remote CLI (syncdb for example)
- "settings_production.py" ("settings_<instance name>.py") is configured on "wsgi.py"

