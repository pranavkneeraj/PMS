# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='contact',
            field=models.CharField(null=True, validators=[django.core.validators.RegexValidator(message='Length has to be 10', regex='^[0-9]{10}$', code='nomatch')], max_length=12, blank=True),
        ),
    ]
