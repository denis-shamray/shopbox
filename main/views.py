import datetime
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from main.models import Good
from main.models import Picture

CART_COOKIE = 'SB-Cart'


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        cookie_cart = self.request.COOKIES.get(CART_COOKIE)
        cookie_cart = json.loads(cookie_cart) if cookie_cart else {}

	cart = {'items': [], 'summ': 0}
        for pk, count in cookie_cart.items():
            good = Good.objects.get(pk=pk)
            cart['items'].append({
                'count': count,
                'good': good
            })
            cart['summ'] += good.price * count

        url_name = resolve(self.request.path).url_name
        context['url_name'] = url_name
        context['goods'] = Good.objects.all()
        context['cart'] = cart
        return context


class IndexView(BaseView):
    template_name = "index.html"


class PreviewView(BaseView):
    template_name = "preview.html"

    def get_context_data(self, pk, **kwargs):
        pk = int(pk)
        context = super(PreviewView, self).get_context_data(**kwargs)
        context['good'] = Good.objects.get(pk=pk)
        return context


class NewsView(BaseView):
    template_name = "news.html"


class AboutView(BaseView):
    template_name = "about.html"


class ContactView(BaseView):
    template_name = "contact.html"


class DeliveryView(BaseView):
    template_name = "delivery.html"


class LoginView(BaseView):
    template_name = "login.html"


class FormView(BaseView):
    template_name = "form_zakaz.html"


class PictureView(View):
    def get(self, request, pk, *args, **kwargs):
        picture = Picture.objects.get(pk=pk)
        image_file = picture.image.file
        return HttpResponse(image_file.read(), image_file.mimetype)


class CartAddView(View):
    def get(self, request, pk, *args, **kwargs):
        good = Good.objects.get(pk=pk)

        return HttpResponse(image_file.read(), image_file.mimetype)


class CartAddRedirectView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'main-cart-add'


    def get(self, request, pk, *args, **kwargs):
        good = get_object_or_404(Good, pk=pk)
        response = super(CartAddRedirectView, self).get(request, *args, **kwargs)

        cart = self.request.COOKIES.get(CART_COOKIE)
        cart = json.loads(cart) if cart else {}

        if pk in cart:
            cart[pk] += 1
        else:
            cart[pk] = 1

        max_age = 7 * 24 * 60 * 60  #one week
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie(CART_COOKIE, json.dumps(cart), max_age=max_age, expires=expires)
        return response

    def get_redirect_url(self, url, *args, **kwargs):
        return reverse(url, kwargs=kwargs)
