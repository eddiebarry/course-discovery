# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-04 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0049_courserun_eligible_for_financial_aid'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='profile_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]