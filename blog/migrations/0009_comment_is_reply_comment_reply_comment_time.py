# Generated by Django 5.2.1 on 2025-05-23 12:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_comments_number_alter_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_reply',
            field=models.BooleanField(default=False, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
