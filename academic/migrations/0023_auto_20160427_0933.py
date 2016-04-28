# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0022_auto_20160427_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetail',
            name='ug_course',
            field=models.CharField(choices=[('Bsc(Computer Science)', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')], max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 9, 33, 45, 974047, tzinfo=utc)),
        ),
    ]
