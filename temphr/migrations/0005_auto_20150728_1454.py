# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('temphr', '0004_auto_20150728_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(related_name='user_candidate', default=None, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employer',
            name='user',
            field=models.OneToOneField(related_name='user_employer', default=None, to=settings.AUTH_USER_MODEL),
        ),
    ]
