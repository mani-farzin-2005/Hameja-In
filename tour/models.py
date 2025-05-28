from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_ckeditor_5.fields import CKEditor5Field

from hotel.models import Hotel
# Create your models here.

class Tagss(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TourGroup(models.Model):
    title = models.CharField(max_length=100)
    content = CKEditor5Field('Text', config_name='extends')
    tags = models.ManyToManyField(Tagss, blank=True)
    last_update=models.DateTimeField(default=timezone.now(),editable=False)
    def get_absolute_url(self):
        return reverse('tour:package', args=[self.id])

    def __str__(self):
        return self.title
    def save(self, *args,**kwargs):
        self.last_update = timezone.now()
        super().save(*args,**kwargs)

class Document(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rating(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],default=1)

class Flight(models.Model):

    company_name = models.CharField(max_length=100)
    start_hour = models.TimeField(default=timezone.now)
    reach_hour = models.TimeField(default=timezone.now)


class Tour(models.Model):
    name = models.CharField(max_length=100)
    image =models.ImageField(upload_to='tour/single-tour/' , null=True)
    tour_group = models.ForeignKey('TourGroup', on_delete=models.SET_NULL, blank=True, null=True, default=None, related_name='subtours' )
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    start_date = models.DateField(default=timezone.now)
    return_date = models.DateField(default=timezone.now)
    flight_go = models.OneToOneField(Flight, null=True, blank=True, on_delete=models.SET_NULL , related_name='flight_go')
    flight_return = models.OneToOneField(Flight, null=True, blank=True, on_delete=models.SET_NULL , related_name='flight_return')
    document = models.ManyToManyField(Document)
    last_update = models.DateTimeField(default=timezone.now)
    comments = models.BooleanField(default=True)
    hotell = models.ManyToManyField(Hotel,related_name='tourss')
    tags = models.ManyToManyField(Tagss, blank=True)
    ratings = models.ManyToManyField(Rating,blank=True,editable=False)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('tour:tour', args=[self.id])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        rating_values = set(hotel.rating for hotel in self.hotell.all())

        for value in rating_values:
            rating_obj = Rating.objects.create(rating=value)
            self.ratings.add(rating_obj)

        self.last_update = timezone.now()
        super().save(*args, **kwargs)


class Service(models.Model):
    name = models.CharField(max_length=100)
    tour = models.ForeignKey('Tour' , on_delete=models.CASCADE,related_name='services')

    def __str__(self):
        return self.name


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(max_length=1000)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    display = models.BooleanField(default=False)
    time = models.DateTimeField(editable=False, null=True)
    reply = models.ForeignKey('Comment', null=True, blank=True, on_delete=models.CASCADE , related_name='repliments')
    is_reply = models.BooleanField(null=True,default=False)

    def __str__(self, *args, **kwargs):
        return f'comment,{self.tour}'

    def save(self, *args, **kwargs):
        if not self.reply:
            self.is_reply =False
        else: self.is_reply =True
        self.time = timezone.now()
        super().save(*args, **kwargs)


class Suggestion_pack(models.Model):
    name = models.CharField(max_length=150)
    tours = models.ManyToManyField(Tour)

    def __str__(self):
        return self.name