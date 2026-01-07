from django.contrib import admin
from django.urls import path, include
from hexlet_django_blog.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("articles/", include("hexlet_django_blog.article.urls")),
    path("admin/", admin.site.urls),
]

