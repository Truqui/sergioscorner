from ckeditor.fields import RichTextField
from django.db import models
from django.core.exceptions import ValidationError

from utils.seo import SEOModel


class Page (SEOModel):
    """A page that only render a html field.
    Also, it has a unique name.
    """
    name = models.CharField(
        'Name',
        max_length=50,
        unique=True
    )
    content = RichTextField(
        blank=True,
        help_text='HTML Code'
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def clean_fields(self, exclude=None):
        self.slug = self.slug.lower()
        if self.slug in ('category', 'article',):
            raise ValidationError(
                {'slug': 'Must be different than "category" and "article"'}
            )
