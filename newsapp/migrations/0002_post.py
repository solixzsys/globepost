# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('pub_date', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField()),
                ('content', models.TextField()),
                ('thumbnail', models.URLField()),
                ('feed_url', models.ForeignKey(to='newsapp.Channel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
