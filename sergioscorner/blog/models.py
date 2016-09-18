from django.db import models


class Category (models.Model):
    """Category of an article"""
    name = models.CharField(
        'Name',
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Article (models.Model):
    """An article is divided in 3 part.
    1- The title.
    2- An introduction of the article. It is used for summaries and is the
    first part of the article.
    3- The text. Is the rest of the article.
    """
    title = models.CharField(
        'Name',
        max_length=50,
        unique=True
    )
    introduction = models.TextField(
        blank=True,
        help_text='First part of the final article. In HTML code.'
    )
    text = models.TextField(
        blank=True,
        help_text='Second part of the final article. In HTML code.'
    )
    categories = models.ManyToManyField(Category, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    last_update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
