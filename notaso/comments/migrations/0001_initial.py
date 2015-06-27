# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('professors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.TextField()),
                ('created_at', models.DateField()),
                ('is_anonymous', models.BooleanField(default=False)),
                ('responsibility', models.IntegerField(null=True)),
                ('personality', models.IntegerField(null=True)),
                ('workload', models.IntegerField(null=True)),
                ('difficulty', models.IntegerField(null=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('professor', models.ForeignKey(to='professors.Professor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
