# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('channel_title', models.CharField(blank=True, max_length=200)),
                ('feed_url', models.URLField()),
                ('category', models.CharField(choices=[('GN', 'General'), ('ENT', 'Entertainment'), ('SPT', 'Sport'), ('FSN', 'Fashion'), ('S&T', 'Science and Technology'), ('WH', 'Weather'), ('CY', 'Currency'), ('ST', 'Stock'), ('Bus', 'Business'), ('FN', 'Financial'), ('LC', 'Local News'), ('WN', 'World News'), ('MC', 'Miscellaneous')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('country_code', models.CharField(blank=True, max_length=5)),
                ('country_name', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('site_name', models.CharField(blank=True, max_length=100)),
                ('site_url', models.CharField(blank=True, max_length=100)),
                ('category', models.CharField(choices=[('GN', 'General'), ('ENT', 'Entertainment'), ('SPT', 'Sport'), ('FSN', 'Fashion'), ('S&T', 'Science and Technology')], max_length=50, default='GN')),
                ('country', models.ForeignKey(to='newsapp.Country')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='channel',
            name='country',
            field=models.ForeignKey(to='newsapp.Country'),
        ),
        migrations.AddField(
            model_name='channel',
            name='site',
            field=models.ForeignKey(to='newsapp.Website'),
        ),
    ]
