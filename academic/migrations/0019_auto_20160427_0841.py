# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0018_auto_20160423_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specialcriteria',
            name='no_of_backlogs',
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='no_of_backlogs',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='academicdetail',
            name='no_of_gap',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='criteria',
            name='no_of_backlogs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 27, 8, 41, 45, 592891, tzinfo=utc)),
        ),
    ]
