from django.test import TestCase
from django.urls.base import reverse

from .factories import CategoryFactory, ArticleFactory


class AllArticlesListViewTest(TestCase):

    def test_article_in_list(self):
        ArticleFactory(title='test', slug='test')

        response = self.client.get(reverse('all-articles'),)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')


class CategoryArticlesListViewTest(TestCase):

    def test_article_in_category_is_in_list(self):
        category = CategoryFactory(name='category', slug='category')
        article = ArticleFactory(title='test', slug='test')
        article.categories.add(category)

        response = self.client.get(
            reverse('category', kwargs={'category': category.name}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    def test_article_not_in_category_is_not_in_list(self):
        category = CategoryFactory(name='category', slug='category')
        article = ArticleFactory(title='test', slug='test')

        response = self.client.get(
            reverse('category', kwargs={'category': category.name}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, article.title)

    def test_raise_404_if_category_not_exist(self):
        response = self.client.get(
            reverse('category', kwargs={'category': 'not-exist'}),
        )
        self.assertEqual(response.status_code, 404)


class ArticleDetailsViewTest(TestCase):

    def test_article_go(self):
        ArticleFactory(title='test', slug='test')

        response = self.client.get(
            reverse('article', kwargs={'slug': 'test'}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
