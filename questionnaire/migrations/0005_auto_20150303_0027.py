# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questionnaire', '0004_questionnaire_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='account',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='subject',
            name='state',
            field=models.CharField(default=b'active', max_length=16, verbose_name='State', choices=[(b'active', 'Active'), (b'inactive', 'Inactive')]),
            preserve_default=True,
        ),
    ]
