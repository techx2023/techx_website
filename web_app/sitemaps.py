from django.contrib.sitemaps import Sitemap
from django.contrib import sitemaps
from django.urls import reverse
from .models import *



class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    protocol = "https"
    changefreq = 'monthly'

    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)