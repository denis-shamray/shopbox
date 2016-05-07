"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from main.views import IndexView
from main.views import PreviewView
from main.views import AboutView
from main.views import ContactView
from main.views import DeliveryView
from main.views import LoginView
from main.views import PictureView
from main.views import CartAddRedirectView
from main.views import FormView
from main.views import ThankyouView
from main.views import ThankyoumsgView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main-index'),
    url(r'^preview/(?P<pk>[0-9]+)$', PreviewView.as_view(), name='main-preview'),
    url(r'^about$', AboutView.as_view(), name='main-about'),
    url(r'^contact$', ContactView.as_view(), name='main-contact'),
    url(r'^delivery$', DeliveryView.as_view(), name='main-delivery'),
    url(r'^login$', LoginView.as_view(), name='main-login'),
    url(r'^picture/(?P<pk>[0-9]+)$', PictureView.as_view(), name='main-picture'),
    url(r'^cart/add/(?P<pk>[0-9]+)/(?P<url>[^\/]+)$', CartAddRedirectView.as_view(), name='main-cart-add'),
    url(r'^cart/add/(?P<pk>[0-9]+)/(?P<url>[^\/]+)/(?P<url_pk>[0-9]+)$', CartAddRedirectView.as_view(), name='main-cart-add-pk'),
    url(r'^form$', FormView.as_view(), name='main-form'),
    url(r'^category/(?P<category_pk>[0-9]+)$', IndexView.as_view(), name='main-category'),
    url(r'^thankyou$', ThankyouView.as_view(), name='main-thankyou'),
    url(r'^thankyoumsg$', ThankyoumsgView.as_view(), name='main-thankyoumsg'),

    url(r'^files/', include('db_file_storage.urls')),
]
