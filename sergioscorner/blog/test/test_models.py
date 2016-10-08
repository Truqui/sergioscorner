from django.test import TestCase

from .factories import CategoryFactory, ArticleFactory
from ..models import Category, Article


class CategoryModelTest(TestCase):

    def test_category_creation(self):
        category = CategoryFactory()
        self.assertTrue(isinstance(category, Category))
        self.assertEqual(str(category), category.name)

    def test_category_slug_must_be_lowercase(self):
        category = CategoryFactory(slug='Slug')
        category.clean_fields()
        self.assertEqual(category.slug, 'slug')


class ArticleModelTest(TestCase):

    def test_article_creation(self):
        article = ArticleFactory()
        self.assertTrue(isinstance(article, Article))
        self.assertEqual(str(article), article.title)

    def test_category_slug_must_be_lowercase(self):
        article = ArticleFactory(slug='Slug')
        article.clean_fields()
        self.assertEqual(article.slug, 'slug')
