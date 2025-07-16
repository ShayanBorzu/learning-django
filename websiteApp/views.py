from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return  render(request, "contact.html")


def http_test(request):
    return HttpResponse("<h1>Http respond successful</h1>")


def json_test(request):
    return JsonResponse({"test": "success"})
