# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-15 08:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apt_repositories', '0002_auto_20151213_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('version', models.CharField(max_length=32)),
                ('arch', models.CharField(max_length=8)),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apt_repositories.Package')),
            ],
        ),
    ]
