# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0003_remove_questionnaire_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='language',
            field=models.ForeignKey(default=1, to='questionnaire.Language'),
            preserve_default=False,
        ),
    ]
