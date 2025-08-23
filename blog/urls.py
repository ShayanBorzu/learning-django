from django.urls import path
from blog.views import blog_index, blog_about, test

app_name = "blog"

urlpatterns = [
    path("", blog_index, name="blog_index"),
    path("about/<int:pk>/", blog_about, name="blog_about"),
    path("category/<str:cat_name>/", blog_index, name="blog_category"),
    path("author/<str:author>/", blog_index, name="blog_author"),
    
]