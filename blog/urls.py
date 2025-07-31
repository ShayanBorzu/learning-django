from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("about/", blog_about, name="blog_about"),
    path("test", test, name="test" )
]
