from django.shortcuts import redirect
from django.urls import reverse
from django.views import View
from hexlet_django_blog.article.models import Article

class IndexView(View):
    def get(self, request, *args, **kwargs):
        latest_article = Article.objects.last()  # последняя добавленная статья
        if latest_article:
            return redirect(reverse("article", kwargs={"id": latest_article.id}))
        return redirect(reverse("articles"))  # если статей нет
