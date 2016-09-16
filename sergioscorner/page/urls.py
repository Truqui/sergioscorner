from django.conf.urls import url
from django.contrib import admin

from .views import HtmlPageView


admin.autodiscover()

urlpatterns = [
    url(r'^$', HtmlPageView.as_view(), name="home"),
]
