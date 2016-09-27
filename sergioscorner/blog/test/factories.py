import factory

from ..models import Category, Article


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Category %s' % n)
    slug = factory.Sequence(lambda n: 'category-slug-%s' % n)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ('title', 'introduction', 'text',)

    title = factory.Sequence(lambda n: 'Article %s' % n)
    introduction = factory.Sequence(lambda n: '<p>Introduction %s</p>' % n)
    text = factory.Sequence(lambda n: '<p>Text %s</p>' % n)
    slug = factory.Sequence(lambda n: 'article-slug-%s' % n)
