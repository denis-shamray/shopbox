from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views.generic import View
from django.core.urlresolvers import resolve
from main.models import Good
from main.models import Picture


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        url_name = resolve(self.request.path).url_name
        context['url_name'] = url_name
        context['goods'] = Good.objects.all()
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


class PictureView(View):
    def get(self, request, pk, *args, **kwargs):
        picture = Picture.objects.get(pk=pk)
        image_file = picture.image.file
        return HttpResponse(image_file.read(), image_file.mimetype)
