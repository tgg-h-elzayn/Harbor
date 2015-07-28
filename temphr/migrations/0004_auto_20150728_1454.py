# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('temphr', '0003_candidate_self_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('user', models.OneToOneField(related_name='user_employer', default=b'', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=6, decimal_places=2)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('review_text', models.TextField(default=b'')),
                ('rating', models.DecimalField(max_digits=3, decimal_places=2)),
                ('reviewer', models.ForeignKey(to='temphr.Employer')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='user',
            field=models.OneToOneField(related_name='user_candidate', default=b'', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='target',
            field=models.ForeignKey(to='temphr.Candidate'),
        ),
        migrations.AddField(
            model_name='job',
            name='employee',
            field=models.ForeignKey(to='temphr.Candidate'),
        ),
        migrations.AddField(
            model_name='job',
            name='employer',
            field=models.ForeignKey(to='temphr.Employer'),
        ),
    ]
