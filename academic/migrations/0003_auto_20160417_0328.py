# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20160417_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusdrive',
            name='company_description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 3, 28, 18, 992373, tzinfo=utc)),
        ),
    ]
