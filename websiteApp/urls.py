from django.urls import path
from websiteApp.views import *

urlpatterns = [
    path("about/", about),
    path("contact/", contact),
    path("http_test/", http_test),
    path("json_test/", json_test),
]
