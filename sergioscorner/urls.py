from django.contrib import admin
from django.urls import re_path, include

from blog.views import AllArticlesListView, CategoryArticlesListView,\
    ArticleDetailsView
from page.views import HtmlPageView


urlpatterns = [
    re_path(r'^$', AllArticlesListView.as_view(), name="all-articles"),
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^(?P<slug>[\w|-]+)/$', HtmlPageView.as_view(), name="article"),
    re_path(
        r'^category/(?P<category_slug>[\w|-]+)/$',
        CategoryArticlesListView.as_view(),
        name="category"
    ),
    re_path(
        r'^article/(?P<slug>[\w|-]+)/$',
        ArticleDetailsView.as_view(),
        name="article"
    )
]
