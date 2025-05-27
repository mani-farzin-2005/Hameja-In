from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone
import subprocess
import os


# Create your models here.


class Author(models.Model):
    person = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.person.username


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    video_file = models.FileField(
        upload_to='videos/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'webm'])]
        , null=True,blank=True
    )

    content = CKEditor5Field('Text', config_name='extends')
    views = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tags, blank=True)
    image = models.ImageField(upload_to='posts/')
    link_to_other_site = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)

    author = models.ForeignKey('Author', models.CASCADE)
    status = models.BooleanField(default=False)

    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)

    comments = models.BooleanField(default=True)
    comments_number = models.PositiveIntegerField(default=0)
    instagram = models.URLField(null=True)
    linkdin = models.URLField(null=True)
    twitter = models.URLField(null=True)
    facebook = models.URLField(null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=1000)
    post = models.ForeignKey('Post', on_delete=models.CASCADE , related_name='comment_owner')
    display = models.BooleanField(default=False)
    time = models.DateTimeField(editable=False, null=True)
    reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)
    is_reply = models.BooleanField(default=False,null=True)

    def __str__(self, *args, **kwargs):
        return f'comment,{self.post}'

    def save(self, *args, **kwargs):
        if not self.reply:
            self.is_reply =False
        else: self.is_reply =True
        self.time = timezone.now()
        super().save(*args, **kwargs)