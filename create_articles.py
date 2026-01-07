from hexlet_django_blog.article.models import Article

Article.objects.create(name='Article 1', body='Content 1')
Article.objects.create(name='Article 2', body='Content 2')
Article.objects.create(name='Article 3', body='Content 3')
Article.objects.create(name='Article 4', body='Content 4')
Article.objects.create(name='Article 5', body='Content 5')

print('5 articles created!')
