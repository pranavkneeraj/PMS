# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import datetime
import django.core.validators
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('first_name', models.CharField(blank=True, verbose_name='First Name', default=None, null=True, max_length=30)),
                ('last_name', models.CharField(blank=True, verbose_name='Last Name', default=None, null=True, max_length=30)),
                ('email', models.EmailField(verbose_name='Email', db_index=True, unique=True, max_length=255)),
                ('is_staff', models.BooleanField(verbose_name='Staff Status', default=False, help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('roll_no', models.IntegerField(blank=True, null=True)),
                ('middle_name', models.CharField(blank=True, null=True, max_length=100)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('contact', models.IntegerField(blank=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 10', regex='^[0-9]{10}$')], null=True)),
                ('is_placed', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', related_query_name='user')),
            ],
            options={
                'abstract': False,
                'ordering': ['email'],
            },
        ),
        migrations.CreateModel(
            name='UniqueRegistration',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('code', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_universal', models.BooleanField(default=False)),
                ('valid_from', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('valid_to', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
