# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0015_auto_20160423_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 23, 0, 32, 57, 426255, tzinfo=utc)),
        ),
    ]
