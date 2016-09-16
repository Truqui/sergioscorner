from django.views.generic.base import TemplateView

from .models import HtmlPage


class HtmlPageView(TemplateView):
    """View for render a HtmlPage object."""
    template_name = 'html_page.html'

    def get_context_data(self, **kwargs):
        context = super(HtmlPageView, self).get_context_data(**kwargs)
        home_page = HtmlPage.objects.get(name='home')
        context['html'] = home_page.html
        return context
