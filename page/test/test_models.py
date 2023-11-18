from django.test import TestCase
from django.core.exceptions import ValidationError

from .factories import HtmlPageFactory
from ..models import HtmlPage


class HtmlPageModelTest(TestCase):

    def test_html_page_creation(self):
        html_page = HtmlPageFactory()
        self.assertTrue(isinstance(html_page, HtmlPage))
        self.assertEqual(str(html_page), html_page.name)

    def test_html_page_slug_cant_be_category(self):
        html_page = HtmlPageFactory(slug='category')
        with self.assertRaises(ValidationError):
            html_page.clean_fields()
