# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields
from django.utils.timezone import utc
from django.conf import settings
import datetime
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDetail',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('student', models.OneToOneField(to=settings.AUTH_USER_MODEL, serialize=False, primary_key=True)),
                ('hsc_marks', models.IntegerField()),
                ('hsc_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hsc_passout_year', models.IntegerField()),
                ('ssc_marks', models.IntegerField()),
                ('ssc_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ssc_passout_year', models.IntegerField()),
                ('ug_course', models.CharField(choices=[('bcs', 'Bsc(Computer Science)'), ('bca', 'BCA'), (('be',), 'BE'), ('other', 'Other')], default='bca', max_length=10)),
                ('ug_marks', models.CharField(max_length=200)),
                ('ug_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ug_no_of_backlogs', models.IntegerField(default=0)),
                ('ug_passout_year', models.CharField(blank=True, max_length=200)),
                ('exprience', models.IntegerField(default=0)),
                ('current_pg_sem', models.CharField(blank=True, null=True, max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CampusDrive',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=200)),
                ('company_description', models.CharField(max_length=200)),
                ('drive_on', models.DateTimeField(default=datetime.datetime(2016, 4, 16, 6, 53, 36, 746608, tzinfo=utc))),
                ('recruitment_type', models.CharField(choices=[('pool', 'Pool'), ('campus', 'Campus')], default='campus', max_length=10)),
                ('course_list', django.contrib.postgres.fields.ArrayField(blank=True, null=True, base_field=models.CharField(max_length=200), size=None)),
                ('batch_year', django.contrib.postgres.fields.ArrayField(blank=True, null=True, base_field=models.IntegerField(), size=None)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('is_interested', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PGSem',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('sem_number', models.IntegerField()),
                ('marks', models.IntegerField()),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('no_of_backlogs', models.IntegerField()),
                ('academic', models.ForeignKey(to='academic.AcademicDetail')),
            ],
        ),
        migrations.CreateModel(
            name='SpecialCriteria',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('id', models.UUIDField(editable=False, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('criteria_for', models.CharField(choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('UG', 'UG'), ('PG', 'PG'), ('Other', 'Other')], default='UG', max_length=10)),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, null=True, max_digits=5)),
                ('no_of_backlogs', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('created_on', models.DateTimeField(db_index=True, auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('deleted_on', models.DateTimeField(blank=True, editable=False, db_index=True, null=True)),
                ('campus_drive', models.OneToOneField(to='academic.CampusDrive', serialize=False, primary_key=True)),
                ('throughout', models.DecimalField(default=0, decimal_places=2, max_digits=5)),
                ('no_of_gap', models.IntegerField(default=0)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Any', 'Any')], default='Any', max_length=10)),
                ('exprience', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='specialcriteria',
            name='campus_drive',
            field=models.ForeignKey(to='academic.CampusDrive'),
        ),
        migrations.AddField(
            model_name='interested',
            name='campus_drive',
            field=models.ForeignKey(to='academic.CampusDrive'),
        ),
        migrations.AddField(
            model_name='interested',
            name='student',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='pgsem',
            unique_together=set([('academic', 'sem_number')]),
        ),
    ]
