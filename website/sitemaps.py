from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
class StaticViewSitemap(Sitemap):
    priority = 0.5

    changefreq = 'daily'

    def items(self):
        return ['website:home','website:contact-us','website:about-us']

    def location(self, item):
        return reverse(item)
class PostViewSiteMap(Sitemap):
    priority = 0.8

    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date

    def location(self, obj):
        return obj.get_absolute_url()
