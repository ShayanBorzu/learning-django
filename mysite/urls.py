from django.contrib import admin
from django.urls import path, include
from websiteApp.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from websiteApp.sitemaps import StaticViewSitemap
from blog.sitemaps import *
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore 
from django.contrib.auth import views as auth_views



# sitemaps = {
#     'static': StaticViewSitemap,
#     'blog': BlogSitemap
# }

# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", include("websiteApp.urls")),
#     path("blog/", include("blog.urls")),
#     path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
#             name='django.contrib.sitemaps.views.sitemap'),
#     path('robots.txt', include('robots.urls')),
#     path('summernote/', include('django_summernote.urls')),
#     path('captcha/', include('captcha.urls')),
#     path("accounts/", include('accounts.urls')),
# ] + debug_toolbar_urls()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import re_path
from .views import coming_soon

urlpatterns = [
    re_path(r'^.*$', coming_soon), 
]+ debug_toolbar_urls()
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
