# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0007_auto_20160420_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academicdetail',
            name='hsc_marks',
        ),
        migrations.RemoveField(
            model_name='academicdetail',
            name='ssc_marks',
        ),
        migrations.RemoveField(
            model_name='academicdetail',
            name='ug_marks',
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='pg_course',
            field=models.CharField(choices=[('MCA', 'MCA'), ('MSc(Computer Science)', 'MSc(Computer Science)'), ('other', 'Other')], max_length=20, default='MCA'),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='pg_passout_year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 8, 58, 26, 148946, tzinfo=utc)),
        ),
    ]
