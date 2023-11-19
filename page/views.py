from django.views.generic.detail import DetailView

from .models import Page


class HtmlPageView(DetailView):
    """View for render a HtmlPage object."""
    model = Page
    template_name = 'page.html'

    def get_context_data(self, **kwargs):
        context = super(HtmlPageView, self).get_context_data(**kwargs)
        context['title_tag'] = self.object.title_tag
        context['description_tag'] = self.object.description_tag
        return context
