# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Block(models.Model):
    namechar = models.CharField(u"名字",
            max_length=40)
    descriptionchar = models.CharField(u"描述",
            max_length=100)
    admin = models.ForeignKey(User, verbose_name="管理员")

    create_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.namechar

    class Meta:
        verbose_name = (u"板块")
        verbose_name_plural = (u"板块")
