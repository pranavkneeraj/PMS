# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import uuid
from django.utils.timezone import utc
import datetime
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDetail',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('student', models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False)),
                ('hsc_marks', models.IntegerField()),
                ('hsc_percentage', models.DecimalField(max_digits=5, decimal_places=2)),
                ('hsc_passout_year', models.IntegerField()),
                ('ssc_marks', models.IntegerField()),
                ('ssc_percentage', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ssc_passout_year', models.IntegerField()),
                ('ug_course', models.CharField(choices=[('bcs', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')], max_length=10, default='bca')),
                ('ug_marks', models.CharField(max_length=200)),
                ('ug_percentage', models.DecimalField(max_digits=5, decimal_places=2)),
                ('ug_passout_year', models.CharField(max_length=200)),
                ('exprience', models.IntegerField()),
                ('current_pg_sem', models.CharField(null=True, blank=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusDrive',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('company_name', models.CharField(max_length=200)),
                ('company_description', models.CharField(max_length=200)),
                ('drive_on', models.DateTimeField(default=datetime.datetime(2016, 4, 12, 18, 2, 55, 962720, tzinfo=utc))),
                ('throughout', models.DecimalField(max_digits=5, null=True, decimal_places=2, blank=True)),
                ('no_of_gap', models.IntegerField(null=True, blank=True)),
                ('batch_year', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.IntegerField(), blank=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Any', 'Any')], max_length=10, default='Any')),
                ('exprience', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('is_interested', models.BooleanField(default=False)),
                ('campus_drive', models.ForeignKey(to='academic.CampusDrive')),
                ('student', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PGSem',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('sem_number', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('percentage', models.DecimalField(max_digits=5, decimal_places=2)),
                ('no_of_backlogs', models.IntegerField()),
                ('academic', models.ForeignKey(to='academic.AcademicDetail')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialCriteria',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(null=True, db_index=True, editable=False, blank=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, editable=False)),
                ('criteria_for', models.CharField(choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('UG', 'UG'), ('PG', 'PG'), ('Other', 'Other')], max_length=10, default='UG')),
                ('percentage', models.DecimalField(max_digits=5, null=True, decimal_places=2, blank=True)),
                ('no_of_backlogs', models.IntegerField(null=True, blank=True)),
                ('campus_drive', models.ForeignKey(to='academic.CampusDrive')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterUniqueTogether(
            name='pgsem',
            unique_together=set([('academic', 'sem_number')]),
        ),
    ]
