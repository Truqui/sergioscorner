from django.views.generic.detail import DetailView

from .models import HtmlPage


class HtmlPageView(DetailView):
    """View for render a HtmlPage object."""
    model = HtmlPage
    template_name = 'html_page.html'

    def get_context_data(self, **kwargs):
        context = super(HtmlPageView, self).get_context_data(**kwargs)
        context['title_tag'] = self.object.title_tag
        context['description_tag'] = self.object.description_tag
        return context
