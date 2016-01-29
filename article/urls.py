from django.conf.urls import url


urlpatterns = [
        url(r'^lists/(?P<block_id>\d+)', "article.views.article_list", name="article_list"),
        url(r'^create/(?P<block_id>\d+)', "article.views.create_article", name="article_create"),
]
