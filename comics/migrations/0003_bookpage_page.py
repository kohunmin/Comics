# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comics', '0002_bookpage_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpage',
            name='page',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
