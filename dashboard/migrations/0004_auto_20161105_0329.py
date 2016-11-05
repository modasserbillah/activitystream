# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_employee_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='modified_by',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_by',
            field=models.CharField(max_length=200, null=True, editable=False),
            preserve_default=True,
        ),
    ]
