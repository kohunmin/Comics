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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('pic_url', models.CharField(max_length=300)),
                ('book_id', models.ForeignKey(to='comics.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('body', models.TextField(max_length=100)),
                ('book_page_id', models.ForeignKey(to='comics.BookPage')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
