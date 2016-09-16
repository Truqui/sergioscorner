import factory

from ..models import HtmlPage


class HtmlPageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HtmlPage
        django_get_or_create = ('name', 'html')

    name = factory.Sequence(lambda n: 'Name %s' % n)
    html = factory.Sequence(lambda n: '<p>Html Code %s</p>' % n)
