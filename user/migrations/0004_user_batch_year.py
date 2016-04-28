# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20160419_0316'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='batch_year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
