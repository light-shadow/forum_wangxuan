# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0003_auto_20160121_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('namechar', models.CharField(max_length=40, verbose_name='\u540d\u5b57')),
                ('descriptionchar', models.CharField(max_length=100, verbose_name='\u63cf\u8ff0')),
                ('create_timestamp', models.DateTimeField(auto_now_add=True)),
                ('last_update_timestamp', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(verbose_name=b'\xe7\xae\xa1\xe7\x90\x86\xe5\x91\x98', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u677f\u5757',
                'verbose_name_plural': '\u677f\u5757',
            },
        ),
        migrations.RemoveField(
            model_name='block1',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='block2',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='block3',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='block4',
            name='admin',
        ),
        migrations.DeleteModel(
            name='block1',
        ),
        migrations.DeleteModel(
            name='block2',
        ),
        migrations.DeleteModel(
            name='block3',
        ),
        migrations.DeleteModel(
            name='block4',
        ),
    ]
