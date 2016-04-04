from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class PreviewView(TemplateView):
    template_name = "preview.html"


class NewsView(TemplateView):
    template_name = "news.html"


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class DeliveryView(TemplateView):
    template_name = "Delivery.html"
