from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title', 'get_categories', 'slug', 'creation_date', 'last_update_date'
    )
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
