# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import djorm_pgfulltext.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('departments', '__first__'),
        ('universities', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=75)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('score', models.FloatField(default=0, editable=False)),
                ('responsibility', models.FloatField(default=0, editable=False)),
                ('personality', models.FloatField(default=0, editable=False)),
                ('workload', models.FloatField(default=0, editable=False)),
                ('difficulty', models.FloatField(default=0, editable=False)),
                ('search_index', djorm_pgfulltext.fields.VectorField(default=b'', serialize=False, null=True, editable=False, db_index=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('department', models.ForeignKey(to='departments.Department')),
                ('university', models.ForeignKey(to='universities.University')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
