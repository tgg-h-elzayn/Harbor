# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temphr', '0002_candidate_join_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='self_description',
            field=models.TextField(default=b''),
        ),
    ]
