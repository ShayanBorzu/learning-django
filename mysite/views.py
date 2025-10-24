
from django.http import HttpResponse

def coming_soon(request):
    return HttpResponse("<h1>به زودی در دسترس خواهد بود</h1><p>لطفا بعدا مراجعه کنید.</p>")
