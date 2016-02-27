# coding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from article.models import Article
from utils.response import json_response
from models import Comment
from utils.paginator import paginate_queryset


@login_required
def create_comment(request):
    article_id = int(request.POST["article_id"])
    to_comment_id = int(request.POST["to_comment_id"])
    content = request.POST["content"].strip()
    article = Article.objects.get(id=article_id)
    comment = Comment(block=article.block, article=article,
              owner=request.user, to_comment_id=to_comment_id,
              content=content)
    comment.save()
    return json_response({})


def comment_list(request, article_id):
    article_id = int(article_id)
    comment_page_no = int(request.GET.get("comment_page_no", 1))
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article=article).order_by("-last_update_timestamp")

    object_list, pagination_data = paginate_queryset(comments, comment_page_no)
    return render_to_response("article_detail.html", {"comments": object_list, "article": article,
                              "pagination": pagination_data},
                              context_instanc=RequestContext(request))
