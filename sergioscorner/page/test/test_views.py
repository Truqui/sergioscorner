from django.test import TestCase
from django.urls.base import reverse

from .factories import HtmlPageFactory


class HtmlPageViewTest(TestCase):

    def test_home_html_page(self):
        HtmlPageFactory(name='home', html='<h1>test</h1>')
        response = self.client.get(reverse('page:home'),)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>test</h1>')
