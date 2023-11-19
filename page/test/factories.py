import factory

from ..models import Page


class PageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Page
        django_get_or_create = ('name', 'content')

    name = factory.Sequence(lambda n: 'Name %s' % n)
    content = factory.Sequence(lambda n: '<p>Html Code %s</p>' % n)
