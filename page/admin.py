from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }


admin.site.register(Page, PageAdmin)
