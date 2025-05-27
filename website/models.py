from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse, NoReverseMatch
from django_ckeditor_5.fields import CKEditor5Field
from solo.models import SingletonModel



class WebInfo(SingletonModel):
    description = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/')
    logo_down = models.ImageField(upload_to='logos/' , null=True)
    news_letter = models.TextField()
    copy_right = models.TextField()
    video_file = models.FileField(
        upload_to='videos/',  null=True,blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4', 'mov', 'avi', 'webm'])]
    )
    thumbnail = models.ImageField(upload_to='thumbnails/',editable=False,null=True)
    index_banner_image = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return 'Web Site Info'


class AboutUs(SingletonModel):
    about_us_small = models.TextField()
    content = CKEditor5Field('Text', config_name='extends' , null=True,default=True)

    def __str__(self):
        return 'About Us Info'

class Advertising(models.Model):
    video_file = models.FileField(
        upload_to='videos/advertising/', null=True, blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])]
    )
    content = models.TextField()



class ContactUs(SingletonModel):
    phone_number = models.CharField(max_length=12)
    assistent_number = models.CharField(max_length=12 , null=True)
    facebook = models.URLField()
    telegram = models.URLField()
    whatsapp = models.URLField()
    instagram = models.URLField()
    twitter = models.URLField()
    youtube = models.URLField()
    address = models.TextField()
    email = models.EmailField()
    location_latitude = models.FloatField(default=35.6950394)
    location_longitude = models.FloatField(default=51.3743092)

    def __str__(self):
        return 'Contact Us Info'


class HeaderObject(models.Model):
    name = models.CharField(max_length=100)
    href = models.CharField(max_length=1000)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True , related_name='childern')
    is_childern = models.BooleanField(default=False)
    dynamic_part = models.CharField(editable=False,default='' , max_length=100)
    def __str__(self):
        return self.name



    def save(self, *args, **kwargs):
        if self.parent is not None:
            self.is_childern = True
        else:
            self.is_childern = False
        if self.href and self.href.startswith('('):
            elements = self.href.strip("()").split(",")
            if len(elements) >= 2:
                tuple_result = tuple(elem.strip(" '\"") for elem in elements)
                self.href = tuple_result[0]
                self.dynamic_part = tuple_result[1]
        super().save(*args, **kwargs)