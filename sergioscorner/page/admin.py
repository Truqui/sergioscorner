from django.contrib import admin

from .models import HtmlPage


class HtmlPageAdmin(admin.ModelAdmin):
    pass

admin.site.register(HtmlPage, HtmlPageAdmin)
