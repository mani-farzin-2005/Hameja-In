# Generated by Django 5.2.1 on 2025-05-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_headerobject_dynamic_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headerobject',
            name='dynamic_part',
            field=models.CharField(default='', editable=False, max_length=100),
        ),
    ]
