from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
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

    class Meta:
        ordering = ['pk']


class PictureImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Picture(models.Model):
    good = models.ForeignKey(Good, related_name="pictures")
    url = models.URLField(max_length=255)
    image = models.ImageField(upload_to='main.PictureImage/bytes/filename/mimetype', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def preview(self):
        url = reverse('main-picture', kwargs={'pk':self.pk})
        return format_html('<a href="{}" target="_blank"><img src="{}" width="160px"></a>', url, url)

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['pk']
