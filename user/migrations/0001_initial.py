# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid
import django.utils.timezone
import django.core.validators
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', help_text='Designates that this user has all permissions without explicitly assigning them.', default=False)),
                ('first_name', models.CharField(verbose_name='First Name', null=True, blank=True, max_length=30, default=None)),
                ('last_name', models.CharField(verbose_name='Last Name', null=True, blank=True, max_length=30, default=None)),
                ('email', models.EmailField(verbose_name='Email', unique=True, max_length=255, db_index=True)),
                ('is_staff', models.BooleanField(verbose_name='Staff Status', help_text='Designates whether the user can log into this admin site.', default=False)),
                ('is_active', models.BooleanField(verbose_name='active', help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', default=True)),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('roll_no', models.IntegerField(null=True, blank=True)),
                ('middle_name', models.CharField(null=True, blank=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('contact', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^[0-9]{10}$')], blank=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user', related_name='user_set', blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', help_text='Specific permissions for this user.', related_query_name='user', related_name='user_set', blank=True, to='auth.Permission')),
            ],
            options={
                'abstract': False,
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='UniqueRegistration',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('code', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_universal', models.BooleanField(default=False)),
                ('valid_from', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('valid_to', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
