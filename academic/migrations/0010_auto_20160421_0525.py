# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0009_auto_20160421_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicdetail',
            name='ug_course',
            field=models.CharField(default='bca', choices=[('Bsc(Computer Science)', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')], max_length=10),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 5, 25, 49, 618382, tzinfo=utc)),
        ),
    ]
