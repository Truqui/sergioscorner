from django.views.generic.list import ListView
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from django.views.generic.detail import DetailView

from .models import Article, Category


class AllArticlesListView(ListView):
    model = Article
    template_name = 'list_articles.html'
    ordering = '-creation_date'


class CategoryArticlesListView(ListView):
    model = Article
    template_name = 'list_articles.html'

    def get_queryset(self):
        try:
            category = Category.objects.get(slug=self.kwargs['category'])
        except ObjectDoesNotExist:
            raise Http404('Category does not exist')
        return Article.objects.filter(
            categories__in=(category,),
        ).order_by('-creation_date')


class ArticleDetailsView(DetailView):
    model = Article
    template_name = 'article.html'
