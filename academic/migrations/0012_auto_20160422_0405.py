# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0011_auto_20160421_0526'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pgsem',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='pgsem',
            name='academic',
        ),
        migrations.RemoveField(
            model_name='academicdetail',
            name='current_pg_sem',
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='pg_percentage',
            field=models.DecimalField(max_digits=5, default=0, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 22, 4, 5, 20, 99824, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='PGSem',
        ),
    ]
