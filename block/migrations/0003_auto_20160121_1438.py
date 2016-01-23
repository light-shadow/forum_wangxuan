# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0002_auto_20160121_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='block2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namechar', models.CharField(max_length=40, verbose_name='\u540d\u5b57')),
                ('descriptionchar', models.CharField(max_length=100, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='block3',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namechar', models.CharField(max_length=40, verbose_name='\u540d\u5b57')),
                ('descriptionchar', models.CharField(max_length=100, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='block4',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namechar', models.CharField(max_length=40, verbose_name='\u540d\u5b57')),
                ('descriptionchar', models.CharField(max_length=100, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now_add=True)),
                ('admin', models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='block1',
            name='admin',
            field=models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='block1',
            name='descriptionchar',
            field=models.CharField(max_length=100, verbose_name='\u63cf\u8ff0'),
        ),
        migrations.AlterField(
            model_name='block1',
            name='namechar',
            field=models.CharField(max_length=40, verbose_name='\u540d\u5b57'),
        ),
    ]
