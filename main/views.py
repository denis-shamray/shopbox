from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class PreviewView(TemplateView):
    template_name = "preview.html"


class NewsView(TemplateView):
    template_name = "news.html"