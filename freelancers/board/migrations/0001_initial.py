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
            name='Posting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True, max_length=200)),
                ('body', models.CharField(default=b' ', max_length=1000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(related_name='author', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('chosen', models.ForeignKey(related_name='chosen', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(default=b' ', max_length=1000)),
                ('author', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('theposting', models.ForeignKey(blank=True, to='board.Posting', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
