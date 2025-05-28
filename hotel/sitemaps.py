from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Hotel
class HotelViewSitemaps(Sitemap):
    priority = 0.7

    changefreq = 'daily'

    def items(self):
        return Hotel.objects.all()

    def lastmod(self, obj):
        return obj.last_update

    def location(self, obj):
        return obj.get_absolute_url()