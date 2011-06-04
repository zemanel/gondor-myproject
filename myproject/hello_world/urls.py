from django.conf.urls.defaults import *
from hello_world.views import say_hello

urlpatterns = patterns('',
    url(r'', say_hello, name='say-hello'),
)
