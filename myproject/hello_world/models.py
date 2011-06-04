from django.db import models
from django.utils.translation import ugettext_lazy as _

class Message(models.Model):
    message = models.CharField(_('message'), max_length=30)
