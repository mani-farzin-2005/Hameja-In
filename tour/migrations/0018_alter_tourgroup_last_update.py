# Generated by Django 5.2.1 on 2025-05-28 08:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0017_tourgroup_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourgroup',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2025, 5, 28, 8, 44, 27, 938594, tzinfo=datetime.timezone.utc), editable=False),
        ),
    ]
