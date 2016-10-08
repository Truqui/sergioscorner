from django.contrib import admin

from .models import HtmlPage


class HtmlPageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(HtmlPage, HtmlPageAdmin)
