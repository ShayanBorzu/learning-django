from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

# Create your views here.
def blog_index(request):
    posts = posts = Post.objects.filter(status=1, published__lte=timezone.now())
    return render(request, "blog/blog_index.html",{'posts': posts})


def blog_about(request):
    return render(request, "blog/blog_about.html")

def test(request):
    posts = Post.objects.all()
    return render(request, "blog/test.html", {'posts': posts})