# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0006_auto_20150305_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='subject',
            field=models.ForeignKey(help_text='The user who supplied this answer', to='questionnaire.Subject'),
            preserve_default=True,
        ),
    ]
