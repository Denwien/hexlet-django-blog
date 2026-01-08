from django.shortcuts import render
from django.views import View

from hexlet_django_blog.article.models import Article


class ArticleIndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            {
                "articles": articles,
            },
        )
