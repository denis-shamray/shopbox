from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.html import format_html
import json


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Good(models.Model):
    title = models.CharField(max_length=255)
    short = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, related_name="category", null=True, blank=True, default=None)

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
    image = models.ImageField(upload_to='main.PictureImage/bytes/filename/mimetype', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse('main-picture', kwargs={'pk':self.pk})

    @property
    def preview(self):
        return format_html('<a href="{}" target="_blank"><img src="{}" width="160px"></a>', self.url, self.url)

    @property
    def good_title(self):
        return self.good.title

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['pk']


class Zakaz(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    cart = models.TextField()
    state =  models.CharField(max_length=255, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Msg(models.Model):
    username = models.CharField(max_length=255)
    useremail = models.CharField(max_length=255)
    userphone = models.CharField(max_length=255)
    usermsg = models.TextField()
    state =  models.CharField(max_length=255, default="new")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SmsImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Sms(models.Model):
    username = models.CharField(max_length=255)
    useremail = models.CharField(max_length=255)
    userphone = models.CharField(max_length=255)
    userplace = models.CharField(max_length=255)
    state =  models.CharField(max_length=255, default="new")
    userfile = models.ImageField(upload_to='main.SmsImage/bytes/filename/mimetype', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class IcoImage(models.Model):
    bytes = models.TextField()
    filename = models.CharField(max_length=255)
    mimetype = models.CharField(max_length=50)


class Ico(models.Model):
    image = models.ImageField(upload_to='main.IcoImage/bytes/filename/mimetype', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def url(self):
        return reverse('main-ico', kwargs={'pk':self.pk})

    @property
    def preview(self):
        return format_html('<a href="{}" target="_blank"><img src="{}" width="160px"></a>', self.url, self.url)

    def __unicode__(self):
        return self.url

    class Meta:
        ordering = ['pk']


