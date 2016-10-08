from django.conf.urls import url
from django.contrib import admin

from blog.views import AllArticlesListView, CategoryArticlesListView,\
    ArticleDetailsView
from page.views import HtmlPageView


urlpatterns = [
    url(r'^$', AllArticlesListView.as_view(), name="all-articles"),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[\w|-]+)/$', HtmlPageView.as_view(), name="article"),
    url(
        r'^category/(?P<category_slug>[\w|-]+)/$',
        CategoryArticlesListView.as_view(),
        name="category"
    ),
    url(
        r'^article/(?P<slug>[\w|-]+)/$',
        ArticleDetailsView.as_view(),
        name="article"
    ),
]
