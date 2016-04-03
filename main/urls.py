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
from main.views import NewsView
from main.views import AboutView
from main.views import ContactView
from main.views import DeliveryView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='main-index'),
    url(r'^preview$', PreviewView.as_view(), name='main-preview'),
    url(r'^news$', NewsView.as_view(), name='main-news'),
    url(r'^about$', AboutView.as_view(), name='main-about'),
    url(r'^contact$', ContactView.as_view(), name='main-contact'),
    url(r'^delivery$', DeliveryView.as_view(), name='main-delivery'),
]

