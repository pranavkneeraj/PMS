# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_auto_20160418_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 19, 3, 16, 10, 289138, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='specialcriteria',
            name='criteria_for',
            field=models.CharField(choices=[('ssc', 'SSC'), ('ssc', 'HSC'), ('ug', 'UG'), ('pg', 'PG'), ('other', 'Other')], default='ug', max_length=10),
        ),
    ]
