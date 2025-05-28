from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Tour , TourGroup
class TourViewSitemap(Sitemap):
    priority = 0.5

    changefreq = 'daily'

    def items(self):
        return ['tour:all-tour']

    def location(self, item):
        return reverse(item)
class SingleTourViewSiteMap(Sitemap):
    priority = 0.9

    changefreq = 'daily'

    def items(self):
        return Tour.objects.all()

    def lastmod(self, obj):
        return obj.last_update

    def location(self, obj):
        return obj.get_absolute_url()
class PackageTourViewsSitemap(Sitemap):
    priority = 0.8

    changefreq = 'daily'

    def items(self):
        return TourGroup.objects.all()

    def lastmod(self, obj):
        return obj.last_update

    def location(self, obj):
        return obj.get_absolute_url()