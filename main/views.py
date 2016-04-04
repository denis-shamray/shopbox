from django.views.generic import TemplateView
from django.core.urlresolvers import resolve


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        url_name = resolve(self.request.path).url_name
        context['url_name'] = url_name
        return context


class IndexView(BaseView):
    template_name = "index.html"


class PreviewView(BaseView):
    template_name = "preview.html"


class NewsView(BaseView):
    template_name = "news.html"


class AboutView(BaseView):
    template_name = "about.html"


class ContactView(BaseView):
    template_name = "contact.html"


class DeliveryView(BaseView):
    template_name = "delivery.html"
