from django.shortcuts import get_object_or_404
from django.shortcuts import render_to_response

from hello_world.models import Message

def say_hello(request, template="hello_world/hello.html"):
    message = get_object_or_404(Message, pk=1)
    return render_to_response(template, {
        'message':message.message,
    })