# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0008_auto_20160420_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicdetail',
            name='current_ug_sem',
            field=models.CharField(blank=True, null=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 4, 21, 56, 359999, tzinfo=utc)),
        ),
    ]
