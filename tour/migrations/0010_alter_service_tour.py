# Generated by Django 5.2.1 on 2025-05-22 08:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0009_alter_tour_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='tour',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service', to='tour.tour'),
        ),
    ]
