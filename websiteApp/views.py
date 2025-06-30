from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def home(request):
    return HttpResponse("<h1>Home</h1>")


def about(request):
    return HttpResponse("<h1>You don't know me son.</h1>")


def contact(request):
    return HttpResponse("<h1>Not Available.</h1>")


def http_test(request):
    return HttpResponse("<h1>Http respond successful</h1>")


def json_test(request):
    return JsonResponse({"test": "success"})
