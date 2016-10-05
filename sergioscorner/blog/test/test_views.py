from django.test import TestCase
from django.urls.base import reverse

from .factories import CategoryFactory, ArticleFactory


class AllArticlesListViewTest(TestCase):

    def test_article_in_list(self):
        ArticleFactory(title='test', slug='test')

        response = self.client.get(reverse('all-articles'),)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    def test_all_article_list_has_title_and_description_tags(self):
        response = self.client.get(reverse('all-articles'),)

        self.assertContains(response, '<title>Sergio\'s Corner | Home</title>')
        self.assertContains(
            response,
            '<meta name="description" content="Personal space '
        )


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

    def test_category_has_title_and_description_tags(self):
        category = CategoryFactory(name='category', slug='category')

        response = self.client.get(
            reverse('category', kwargs={'category': category.slug}),
        )
        self.assertContains(
            response,
            '<title>Sergio\'s Corner | ' + category.title_tag + '</title>'
        )
        self.assertContains(
            response,
            '<meta name="description" content="' +
            category.description_tag + '"'
        )


class ArticleDetailsViewTest(TestCase):
    def test_article_work(self):
        ArticleFactory(title='test', slug='test')

        response = self.client.get(
            reverse('article', kwargs={'slug': 'test'}),
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    def test_article_has_title_and_description_tags(self):
        article = ArticleFactory(title='test', slug='test')

        response = self.client.get(
            reverse('article', kwargs={'slug': article.slug}),
        )
        self.assertContains(
            response,
            '<title>Sergio\'s Corner | ' + article.title_tag + '</title>'
        )
        self.assertContains(
            response,
            '<meta name="description" content="' +
            article.description_tag + '"'
        )
