# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_url',
            field=models.URLField(blank=True),
        ),
    ]
