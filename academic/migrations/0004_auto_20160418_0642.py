# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_auto_20160417_0328'),
    ]

    operations = [
        migrations.AddField(
            model_name='campusdrive',
            name='criteria_type',
            field=models.CharField(default='none', choices=[('none', 'No Criteria'), ('general', 'General Criteria'), ('special', 'Special Criteria'), ('both', 'Both')], max_length=20),
        ),
        migrations.AlterField(
            model_name='campusdrive',
            name='drive_on',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 6, 42, 54, 267245, tzinfo=utc)),
        ),
    ]
