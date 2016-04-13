# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('title', models.CharField(null=True, blank=True, max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('catagory', models.CharField(null=True, blank=True, max_length=100)),
                ('display', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
