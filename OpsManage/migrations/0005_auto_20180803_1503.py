# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-08-03 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OpsManage', '0004_auto_20180803_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_config',
            name='project_address',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe4\xbb\x93\xe5\xba\x93\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='project_config',
            name='project_dir',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name=b'\xe4\xbb\xa3\xe7\xa0\x81\xe7\x9b\xae\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='project_config',
            name='project_repertory',
            field=models.CharField(blank=True, default=None, max_length=10, null=True, verbose_name=b'\xe4\xbb\x93\xe5\xba\x93\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='project_config',
            name='project_repo_dir',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name=b'\xe6\x9c\xac\xe5\x9c\xb0\xe4\xbb\x93\xe5\xba\x93\xe7\x9b\xae\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='project_config',
            name='project_type',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name=b'\xe7\xbc\x96\xe8\xaf\x91\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='project_config',
            name='project_user',
            field=models.CharField(blank=True, default=None, max_length=50, null=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x96\x87\xe4\xbb\xb6\xe5\xae\xbf\xe4\xb8\xbb'),
        ),
    ]