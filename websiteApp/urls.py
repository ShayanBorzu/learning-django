from django.urls import path
from websiteApp.views import *

app_name = 'websiteApp'

urlpatterns = [
    path("", home, name='index'),
    path("about/", about, name='about'),
    path("contact/", contact, name='contact'),
    path("http_test/", http_test),
    path("json_test/", json_test),
    path('newsletter/', newsletter_view, name='newsletter'),
]