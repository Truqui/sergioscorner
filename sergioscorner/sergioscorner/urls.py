from django.conf.urls import url
from django.contrib import admin

from blog.views import AllArticlesListView, CategoryArticlesListView,\
    ArticleDetailsView


urlpatterns = [
    url(r'^$', AllArticlesListView.as_view(), name="all-articles"),
    url(
        r'^category/(?P<category>[\w|-]+)/$',
        CategoryArticlesListView.as_view(),
        name="category"
    ),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[\w|-]+)/$', ArticleDetailsView.as_view(), name="article"),
]
