# Settings for production

from settings.common import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

#database instance will be configured by local_settings.py

try:
    from local_settings import *
except ImportError:
    pass