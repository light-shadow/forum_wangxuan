from django.conf.urls import url


urlpatterns = [
    url(r'^create/$', "comment.views.create_comment", name="create_comment"),
    url(r'^lists/$', "comment.views.comment_list", name="comment_list"),
]
