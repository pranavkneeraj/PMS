# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0013_auto_20160422_0405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetail',
            name='current_ug_sem',
        ),
        migrations.AlterField(
            model_name='academicdetail',
            name='pg_course',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[('MCA', 'MCA'), ('MSc(Computer Science)', 'MSc(Computer Science)'), ('other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='academicdetail',
            name='ug_course',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[('Bsc(Computer Science)', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')]),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 22, 23, 57, 26, 108465, tzinfo=utc)),
        ),
    ]
