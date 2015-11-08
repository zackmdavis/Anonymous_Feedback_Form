# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackItem',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
    ]
