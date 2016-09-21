from django.contrib import admin

from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        'title', 'get_categories', 'slug', 'creation_date', 'last_update_date'
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
