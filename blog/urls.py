from django.urls import path
from blog.views import *

app_name = "blog"

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("about/<int:pk>/", blog_about, name="blog_about"),
    path("category/<str:cat_name>/", blog_index, name="blog_category"),
    path("tag/<str:tag_name>/", blog_index, name="blog_tag"),
    path("author/<str:author>/", blog_index, name="blog_author"),
    path("search/", blog_search, name="blog_search"),
    path('test/', test_view, name='test_view'),
]