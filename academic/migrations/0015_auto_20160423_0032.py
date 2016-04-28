# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0014_auto_20160422_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetail',
            name='pg_percentage',
            field=models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 23, 0, 32, 49, 150565, tzinfo=utc)),
        ),
    ]
