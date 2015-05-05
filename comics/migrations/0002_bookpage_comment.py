# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pic', models.CharField(max_length=1000)),
                ('book', models.ForeignKey(to='comics.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
                ('date', models.DateTimeField(verbose_name='time added')),
                ('bookpage', models.ForeignKey(to='comics.BookPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
