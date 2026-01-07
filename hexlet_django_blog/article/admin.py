from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке статей
    list_display = ("name", "created_at")

    # Поля, по которым будет работать поиск
    search_fields = ["name", "body"]

    # Фильтр по дате создания статьи
    list_filter = (("created_at", DateFieldListFilter),)
