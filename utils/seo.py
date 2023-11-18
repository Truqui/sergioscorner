from django.db import models


class SEOModel (models.Model):
    """An abstract model class that give title a description tag.
    This fields shoud be load in every view
    """
    title_tag = models.CharField(
        max_length=47,
    )
    description_tag = models.CharField(
        max_length=156,
    )

    class Meta:
        abstract = True


class SEOMixin(object):
    """View mixin which include in context title tah and description tag."""

    def get_context_data(self, **kwargs):
        context = super(SEOMixin, self).get_context_data(**kwargs)
        context['title_tag'] = self.object.title_tag
        return context
