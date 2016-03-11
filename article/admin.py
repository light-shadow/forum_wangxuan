# coding: utf-8
from django.contrib import admin
from models import Article
from comment.models import Comment
# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment
    readonly_fields = ("block", "owner", "content", "status", "last_update_timestamp")  # 设置只读字段
    fieldsets = (
        (u"评论详情", {
            "classes": ('collapse',),
            "fields": ("owner", "content", "status", "last_update_timestamp")
        }),
    )
CommentInline.can_delete = False
CommentInline.max_num = 20
CommentInline.min_num = 0


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "block", "owner", "status", "create_timestamp", "last_update_timestamp")
    search_fields = ["title", "content", ]
    list_filter = ("block", )
    actions = ["make_picked", "make_picked2"]
    inlines = [CommentInline]
    readonly_fields = ("title", "block", "owner", "content", "status", "create_timestamp", "last_update_timestamp")
    fieldsets = (
        (u"文章详情", {
            "classes": ('collapse',),
            "fields": ("title", "owner", "content", "status", "create_timestamp")
        }),
        (u"其他的", {
            "classes": ('collapse',),
            "fields": ("block", "last_update_timestamp")
        }),
    )

    def make_picked(self, request, queryset):
        for a in queryset:
            a.status = 1
            a.save()
    make_picked.short_description = u"设置精华"

    def make_picked2(self, request, queryset):
        for a in queryset:
            a.status = 0
            a.save()
    make_picked2.short_description = u"设置普通"
admin.site.register(Article, ArticleAdmin)
