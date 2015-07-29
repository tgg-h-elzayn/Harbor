# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('temphr', '0006_auto_20150728_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='position',
            field=models.TextField(default=b''),
        ),
    ]
