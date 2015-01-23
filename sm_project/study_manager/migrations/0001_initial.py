# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('site_informed', models.BooleanField(default=False)),
                ('repeat', models.BooleanField(default=False)),
                ('site', models.CharField(max_length=10, blank=True)),
                ('app_date', models.DateField(null=True, blank=True)),
                ('app_time', models.TimeField(null=True, blank=True)),
                ('monitor_allocated', models.IntegerField(null=True, blank=True)),
                ('created', models.DateField()),
                ('created_by', models.CharField(max_length=50, blank=True)),
                ('modified', models.DateField(null=True, blank=True)),
                ('modified_by', models.CharField(max_length=50, blank=True)),
                ('study_phase', models.IntegerField(null=True, blank=True)),
                ('app_status', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gp_name', models.CharField(max_length=50, blank=True)),
                ('created', models.DateField()),
                ('created_by', models.CharField(max_length=50)),
                ('modified', models.DateField(null=True, blank=True)),
                ('modified_by', models.CharField(max_length=50, blank=True)),
                ('gp_code', models.CharField(max_length=8, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('addr1', models.CharField(max_length=50, blank=True)),
                ('addr2', models.CharField(max_length=50, blank=True)),
                ('town', models.CharField(max_length=50, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('post_code', models.CharField(max_length=50, blank=True)),
                ('telephone', models.CharField(max_length=12, blank=True)),
                ('admin_contact_name', models.CharField(max_length=50, blank=True)),
                ('admin_contact_title', models.CharField(max_length=50, blank=True)),
                ('notes', models.TextField(blank=True)),
                ('funding_notes', models.TextField(blank=True)),
                ('full_name', models.CharField(max_length=70, blank=True)),
                ('surgery_lab_id', models.CharField(max_length=50, blank=True)),
                ('surgery_barcode', models.CharField(max_length=25, blank=True)),
                ('study_survey', models.NullBooleanField()),
                ('created', models.DateField()),
                ('created_by', models.CharField(max_length=50, blank=True)),
                ('modified', models.DateField(null=True, blank=True)),
                ('modified_by', models.CharField(max_length=50, blank=True)),
                ('gp_practice_code', models.CharField(max_length=6, blank=True)),
                ('recruitment_surgery', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volunteer_id', models.CharField(max_length=8, blank=True)),
                ('part_id', models.IntegerField(null=True)),
                ('barcode', models.CharField(max_length=50, blank=True)),
                ('nhs_id', models.CharField(max_length=10, blank=True)),
                ('title', models.CharField(max_length=10, blank=True)),
                ('initials', models.CharField(max_length=10, blank=True)),
                ('fore_names', models.CharField(max_length=50, blank=True)),
                ('surname', models.CharField(max_length=50, blank=True)),
                ('dob', models.DateField(null=True, blank=True)),
                ('sex', models.CharField(max_length=1, blank=True)),
                ('addr1', models.CharField(max_length=50, blank=True)),
                ('addr2', models.CharField(max_length=50, blank=True)),
                ('town', models.CharField(max_length=50, blank=True)),
                ('country', models.CharField(max_length=50, blank=True)),
                ('post_code', models.CharField(max_length=50, blank=True)),
                ('home_tel', models.CharField(max_length=50, blank=True)),
                ('work_tel', models.CharField(max_length=50, blank=True)),
                ('mob_tel', models.CharField(max_length=50, blank=True)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('status', models.IntegerField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('reason', models.IntegerField(null=True, blank=True)),
                ('comment', models.TextField(blank=True)),
                ('test_site', models.CharField(max_length=15, blank=True)),
                ('user_name', models.CharField(max_length=50, blank=True)),
                ('edit_mode', models.BooleanField(default=False)),
                ('editor', models.CharField(max_length=50, blank=True)),
                ('modified', models.DateField(null=True, blank=True)),
                ('modified_by', models.CharField(max_length=50, blank=True)),
                ('created', models.DateField(null=True, blank=True)),
                ('created_by', models.CharField(max_length=50, blank=True)),
                ('moved_away', models.NullBooleanField()),
                ('diabetes_diagnosed', models.NullBooleanField()),
                ('gp_id', models.ForeignKey(to='study_manager.GP')),
                ('surgery_id', models.ForeignKey(to='study_manager.Surgery')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='gp',
            name='surgery_id',
            field=models.ForeignKey(to='study_manager.Surgery'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='volunteer_id',
            field=models.ForeignKey(to='study_manager.Volunteer'),
            preserve_default=True,
        ),
    ]
