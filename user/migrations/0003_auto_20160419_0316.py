# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20160417_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_placed',
        ),
        migrations.AddField(
            model_name='user',
            name='placed_in',
            field=models.CharField(default=None, null=True, max_length=100),
        ),
    ]
