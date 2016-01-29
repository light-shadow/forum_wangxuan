# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0004_auto_20160121_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='descriptionchar',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='block',
            old_name='namechar',
            new_name='name',
        ),
    ]
