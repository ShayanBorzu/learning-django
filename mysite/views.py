from django.http import HttpResponse, JsonResponse

def http_test(request):
    return HttpResponse("<h1> Http respond successful</h1>")

def json_test(request):
    return JsonResponse({"test": "success"})