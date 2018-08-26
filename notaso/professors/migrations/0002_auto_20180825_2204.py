# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-25 22:04
from __future__ import unicode_literals

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("professors", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="professor",
            name="search_index",
            field=django.contrib.postgres.search.SearchVectorField(
                editable=False, null=True
            ),
        ),
        migrations.AddIndex(
            model_name="professor",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=[b"search_index"], name="professors__search__8d84b9_gin"
            ),
        ),
    ]
