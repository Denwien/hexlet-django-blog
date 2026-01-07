from django.views.generic import View
from django.shortcuts import redirect
from django.urls import reverse

class IndexView(View):
    def get(self, request):
        # делаем редирект на обратный маршрут "article" с параметрами
        return redirect(reverse("article", kwargs={"tags": "python", "article_id": 42}))
