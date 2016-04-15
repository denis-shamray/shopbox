from __future__ import unicode_literals
from django.db import models
import json


class Good(models.Model):
    title = models.CharField(max_length=255)
    short = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    options_text = models.TextField()
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_options(self):
        return json.loads(self.options_text)

    def get_pictures(self):
        return self.pictures.all()

    def __unicode__(self):
        return self.title


class Picture(models.Model):
    good = models.ForeignKey(Good, related_name="pictures")
    url = models.URLField(max_length=255)
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.url
