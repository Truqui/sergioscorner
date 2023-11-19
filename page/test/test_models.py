from django.test import TestCase
from django.core.exceptions import ValidationError

from .factories import PageFactory
from ..models import Page


class PageModelTest(TestCase):

    def test_page_creation(self):
        page = PageFactory()
        self.assertTrue(isinstance(page, Page))
        self.assertEqual(str(page), page.name)

    def test_page_slug_cant_be_category(self):
        page = PageFactory(slug='category')
        with self.assertRaises(ValidationError):
            page.clean_fields()
