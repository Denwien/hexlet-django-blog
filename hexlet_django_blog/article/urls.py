from django.urls import path
from .views import IndexView, ArticleFormView, ArticleFormEditView, ArticleView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),  # главная страница списка статей
    path("create/", ArticleFormView.as_view(), name="articles_create"),  # создание статьи
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),  # редактирование
    path("<int:id>/", ArticleView.as_view(), name="article"),  # просмотр статьи
]
