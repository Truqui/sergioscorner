from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.views.generic.detail import DetailView

from .models import Article, Category


class AllArticlesListView(ListView):
    model = Article
    template_name = 'list_articles.html'
    ordering = '-creation_date'

    def get_context_data(self, **kwargs):
        context = super(AllArticlesListView, self).get_context_data(**kwargs)
        context['title_tag'] = "Home"
        context['description_tag'] = "Personal space focused on Django, " + \
            "Python and Best Practices. By Sergio González Cruz."
        return context


class CategoryArticlesListView(ListView):
    model = Article
    template_name = 'list_articles.html'

    def get_queryset(self):
        try:
            self.category = Category.objects.get(slug=self.kwargs['category'])
        except ObjectDoesNotExist:
            raise Http404('Category does not exist')

        return Article.objects.filter(
            categories__in=(self.category,),
        ).order_by('-creation_date')

    def get_context_data(self, **kwargs):
        context = super(
            CategoryArticlesListView, self
        ).get_context_data(**kwargs)
        context['title_tag'] = self.category.title_tag
        context['description_tag'] = self.category.description_tag
        return context


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailsView, self).get_context_data(**kwargs)
        context['title_tag'] = self.object.title_tag
        context['description_tag'] = self.object.description_tag
        return context
