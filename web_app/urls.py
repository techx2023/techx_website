from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from .sitemaps import *
from django.conf.urls import handler404

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # main urls
    path('', Index, name="home"),
    path('contact', contactUs, name="contactez-nous"),
    path('service', OurServices, name="our-services"),
    path('about', About, name="about"),
    path('realisation', Realisation, name="realisation"),

    # Sitemaps
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# handling the 404 error
handler404 = Erreur404