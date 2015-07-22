# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0003_post_post_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='site',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
