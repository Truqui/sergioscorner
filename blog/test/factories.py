import factory

from ..models import Category, Article


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
        django_get_or_create = ('name',)

    name = factory.Sequence(lambda n: 'Category %s' % n)
    slug = factory.Sequence(lambda n: 'category-slug-%s' % n)
    title_tag = factory.Sequence(lambda n: 'Category title %s' % n)
    description_tag = factory.Sequence(lambda n: 'Category description %s' % n)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ('title', 'introduction', 'content',)

    title = factory.Sequence(lambda n: 'Article %s' % n)
    introduction = factory.Sequence(lambda n: '<p>Introduction %s</p>' % n)
    content = factory.Sequence(lambda n: '<p>Content %s</p>' % n)
    slug = factory.Sequence(lambda n: 'article-slug-%s' % n)
    title_tag = factory.Sequence(lambda n: 'Article title %s' % n)
    description_tag = factory.Sequence(lambda n: 'Article description %s' % n)
