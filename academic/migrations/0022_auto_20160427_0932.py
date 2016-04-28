# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0021_auto_20160427_0928'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetail',
            name='ug_no_of_backlogs',
        ),
        migrations.AlterField(
            model_name='academicdetail',
            name='ug_course',
            field=models.CharField(max_length=20, choices=[('Bsc(Computer Science)', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 9, 32, 57, 770322, tzinfo=utc)),
        ),
    ]
