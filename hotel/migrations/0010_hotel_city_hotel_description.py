# Generated by Django 5.2.1 on 2025-05-23 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0009_comment_is_reply_comment_reply_comment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='hotel',
            name='description',
            field=models.TextField(max_length=150, null=True),
        ),
    ]
