# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0005_auto_20150303_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(help_text='The user who supplied this answer', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='runinfohistory',
            name='subject',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
