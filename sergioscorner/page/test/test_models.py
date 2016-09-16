from django.test import TestCase

from .factories import HtmlPageFactory
from ..models import HtmlPage


class HtmlPageModelTest(TestCase):

    def test_html_page_creation(self):
        html_page = HtmlPageFactory()
        self.assertTrue(isinstance(html_page, HtmlPage))
        self.assertEqual(str(html_page), html_page.name)
