from django.test import TestCase

from .factories import CategoryFactory, ArticleFactory
from ..models import Category, Article


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = CategoryFactory()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), category.name)


class ArticleModelTest(TestCase):

    def test_article_creation(self):
        article = ArticleFactory()
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(str(article), article.title)
