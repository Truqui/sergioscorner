from django.db import models


class HtmlPage (models.Model):
    """A page that only render a html field.
    Also, it has an unique name
    """
    name = models.CharField(
        'Name',
        max_length=50,
        unique=True
    )
    html = models.TextField(
        blank=True,
        help_text='HTML Code'
    )

    def __str__(self):
        return self.name
