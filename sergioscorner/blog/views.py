from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Article


class ListArticlesView(ListView):
    model = Article
    template_name = 'list_articles.html'
    ordering = '-creation_date'

    def get_context_data(self, **kwargs):
        context = super(ListArticlesView, self).get_context_data(**kwargs)
        return context
