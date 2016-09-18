from django.contrib import admin

from .models import Category, Article


class CategoryAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'get_categories', 'creation_date', 'last_update_date'
    )

    def get_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
