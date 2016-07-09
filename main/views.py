from copy import copy
import datetime
import json
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import resolve
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

from main.models import Good
from main.models import Picture
from main.models import Category
from main.models import Zakaz
from main.models import Msg
from main.models import Ico
from main.models import Sms, SmsImage
from main.models import Variable
                                                 

CART_COOKIE = 'SB-Cart'


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)

        cookie_cart = self.request.COOKIES.get(CART_COOKIE)
        cookie_cart = json.loads(cookie_cart) if cookie_cart else {}

        cart = {'items': [], 'summ': 0}
        prices = {}
        for pk, count in cookie_cart.items():
            good = Good.objects.get(pk=pk)
            cart['items'].append({
                'count': count,
                'good': good
            })
            prices[pk] = float(good.price)
            cart['summ'] += good.price * count

        url_name = resolve(self.request.path).url_name
        context['url_name'] = url_name
        context['goods'] = Good.objects.all()
        context['random_goods'] = Good.objects.all().order_by("?")
        context['categories'] = Category.objects.all()
        context['cart'] = cart
        context['cart_json'] = json.dumps({
            'items': cookie_cart,
            'prices': prices
        })
        return context


class IndexView(BaseView):
    template_name = "index.html"

    def get_context_data(self, category_pk=None, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs) 
        if category_pk:
            category_pk = int(category_pk)
            context['goods'] = Good.objects.filter(category__pk=category_pk)
        return context

    def get(self, request, *args, **kwargs):
        try:
            index_counter = Variable.objects.get(name='index_counter')
        except Variable.DoesNotExist as error:
            index_counter = Variable(name='index_counter', value="0", description="Views counter for an index page")
        index_counter.value = str(int(index_counter.value)+1)
        index_counter.save()
        return super(IndexView, self).get(request, *args, **kwargs)

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

    def post(self, request, *args, **kwargs):
        fields = ['username', 'useremail', 'userphone', 'usermsg']
        params = {f:request.POST[f] for f in fields}
        msg = Msg.objects.create(**params)

        response = HttpResponse(status=302)
        response['Location'] = reverse('main-thankyoumsg')
        return response


class DeliveryView(BaseView):
    template_name = "delivery.html"


class LoginView(BaseView):
    template_name = "login.html"


class FormView(BaseView):
    template_name = "form_zakaz.html"

    def post(self, request, *args, **kwargs):
        fields = ['firstname', 'lastname', 'tel', 'place', 'cart']
        params = {f:request.POST[f] for f in fields}
        zakaz = Zakaz.objects.create(**params)

        message = "New zakaz!"
        send_mail("test message", message, 'shopboxua@gmail.com', ['shopboxua@gmail.com'], fail_silently=False) 

        response = HttpResponse(status=302)
        response['Location'] = reverse('main-thankyou')

        max_age = 0  #one week
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie(CART_COOKIE, "{}", max_age=max_age, expires=expires)
        return response


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
        kwargs=copy(kwargs)
        if 'url_pk' in kwargs:
            kwargs['pk'] = kwargs.pop('url_pk')
        return reverse(url, kwargs=kwargs)


class ThankyouView(BaseView):
    template_name = "thankyou.html"


class ThankyoumsgView(BaseView):
    template_name = "thankyoumsg.html"


class ThankyouicoView(BaseView):
    template_name = "thankyouico.html"

class PortraitView(BaseView):
    template_name = "portrait.html"

    def get_context_data(self, **kwargs):
        context = super(PortraitView, self).get_context_data(**kwargs)
        context['icos'] = Ico.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        fields = ['username', 'useremail', 'userphone', 'userplace']
        params = {f:request.POST[f] for f in fields}

        sms = Sms.objects.create(**params)
        if 'userfile' in request.FILES:
            userfile = request.FILES['userfile']
            sms.userfile.save(name=userfile.name, content=userfile, save=False)
            sms.save()

        response = HttpResponse(status=302)
        response['Location'] = reverse('main-thankyouico')
        return response


class IcoView(View):
    def get(self, request, pk, *args, **kwargs):
        ico = Ico.objects.get(pk=pk)
        image_file = ico.image.file
        return HttpResponse(image_file.read(), image_file.mimetype)
