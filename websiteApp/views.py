from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, "websiteApp/index.html")


def about(request):
    return render(request, "websiteApp/about.html")


def contact(request):
    return  render(request, "websiteApp/contact.html")


def http_test(request):
    return HttpResponse("<h1>Http respond successful</h1>")


def json_test(request):
    return JsonResponse({"test": "success"})
