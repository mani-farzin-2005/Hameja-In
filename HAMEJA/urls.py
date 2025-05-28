"""
URL configuration for HAMEJA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website.views import p404
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from website.sitemaps import StaticViewSitemap,PostViewSiteMap
from hotel.sitemaps import HotelViewSitemaps
from tour.sitemaps import TourViewSitemap,PackageTourViewsSitemap,SingleTourViewSiteMap


sitemaps_dict ={
    'static':StaticViewSitemap,'posts':PostViewSiteMap,'hotels':HotelViewSitemaps,'tour-suggestions':TourViewSitemap,
    'packages':PackageTourViewsSitemap,'tours':SingleTourViewSiteMap
}

handler404 = p404

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("ckeditor5/", include('django_ckeditor_5.urls')),
                  path("" , include('website.urls',namespace='website')),
                  path("category/blog/" , include('blog.urls')),
                  path("tours/" , include('tour.urls')),
                  path("hotel/" , include('hotel.urls')),
                  path("robots.txt", include("robots.urls")),
                  path('sitemap.xml', sitemap, {'sitemaps': sitemaps_dict}, name='sitemap'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

