import datetime

from django.db import models

from utils.seo import SEOModel


class Category (SEOModel):
    """Category of an article"""
    name = models.CharField(
        'Name',
        max_length=50,
        unique=True
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        self.slug = self.slug.lower()


class Article (SEOModel):
    """An article is divided in 3 part.
    1- The title.
    2- An introduction of the article. It is used for summaries and is the
    first part of the article.
    3- The text. Is the rest of the article.
    """
    title = models.CharField(
        'Title',
        max_length=150,
        unique=True
    )
    introduction = models.TextField(
        blank=True,
        help_text='First part of the final article. In HTML code.'
    )
    content = models.TextField(
        blank=True,
        help_text='Second part of the final article. In HTML code.'
    )
    categories = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(unique=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_categories(self):
        return ", ".join([category.name for category in self.categories.all()])

    def is_updated(self):
        date_creation_plus = self.creation_date + datetime.timedelta(seconds=1)
        if date_creation_plus < self.last_update_date:
            return True
        return False

    def clean_fields(self, exclude=None):
        self.slug = self.slug.lower()
