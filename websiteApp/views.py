from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from django.utils import timezone  

def home(request):
    posts = Post.objects.filter(status=1, published__lte=timezone.now()).order_by('-published')[:6]
    return render(request, "websiteApp/index.html", {'posts': posts})       


def about(request):
    return render(request, "websiteApp/about.html")


def contact(request):
    return  render(request, "websiteApp/contact.html")


def http_test(request):
    return HttpResponse("<h1>Http respond successful</h1>")


def json_test(request):
    return JsonResponse({"test": "success"})
