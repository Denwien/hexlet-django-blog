from django.http import HttpResponse
from django.views import View

class ArticleIndexView(View):
    def get(self, request, tags, article_id):
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")
