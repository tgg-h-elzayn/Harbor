# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('temphr', '0007_job_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.ForeignKey(related_name='user_candidate', to=settings.AUTH_USER_MODEL),
        ),
    ]
