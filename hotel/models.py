from django.utils import timezone

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django_ckeditor_5.fields import CKEditor5Field
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
# Create your models her


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)
    main_image = models.ImageField(upload_to='hotel/' , null=True)
    picture1 = models.ImageField(upload_to='hotel/', null=True)
    picture2 = models.ImageField(upload_to='hotel/', null=True)
    picture3 = models.ImageField(upload_to='hotel/', null=True)
    picture4 = models.ImageField(upload_to='hotel/', null=True)
    picture5 = models.ImageField(upload_to='hotel/', null=True)
    picture6 = models.ImageField(upload_to='hotel/', null=True)
    picture7 = models.ImageField(upload_to='hotel/', null=True)
    content = CKEditor5Field('Text', config_name='extends')
    service = models.ImageField(blank=True,null=True , upload_to='service/')
    service_low = models.ImageField(blank=True,null=True , editable=False , upload_to='service/low/')
    service_medium = models.ImageField(blank=True,null=True,editable=False , upload_to='service/medium/')
    address = models.CharField(max_length=300)
    email = models.URLField()
    website = models.URLField(blank=True,null=True)
    phone_number = models.CharField(max_length=20)
    latitude = models.FloatField(default=35.6950394)
    longitude = models.FloatField(default=51.3743092)
    comments = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=True)
    price = models.PositiveIntegerField(default=100000)
    city = models.CharField(max_length=100 , null=True)
    description = models.TextField(max_length=150 , null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.service_low = self.service
        self.service_medium = self.service
        super().save(*args, **kwargs)


class Service_Hotel(models.Model):
    name = models.CharField(max_length=100)
    tour = models.ForeignKey('Hotel' , on_delete=models.CASCADE ,related_name='hotelll')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=1000)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    display = models.BooleanField(default=False)
    time = models.DateTimeField(editable=False, null=True)
    reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE)
    is_reply = models.BooleanField(default=False,editable=False,null=True)

    def __str__(self, *args, **kwargs):
        return f'comment,{self.hotel}'

    def save(self, *args, **kwargs):
        if not self.reply:
            self.is_reply =False
        else: self.is_reply =True
        self.time = timezone.now()
        super().save(*args, **kwargs)
