from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, HttpRequest
from blog.models import Post
from django.utils import timezone  
from websiteApp.form import ContactForm, NewsLetterForm
from django.contrib import messages

def home(request):
    posts = Post.objects.filter(status=1, published__lte=timezone.now()).order_by('-published')[:6]
    return render(request, "websiteApp/index.html", {'posts': posts})       


def about(request):
    return render(request, "websiteApp/about.html")


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False) 
            instance.name = "unknown"
            if not instance.subject:
                instance.subject = "-empty-"
            instance.save()
            messages.add_message(request, messages.SUCCESS, 'Successful.')
        else:
            messages.add_message(request, messages.ERROR, 'Error encountered.')
            
            
    form = ContactForm()
    return  render(request, "websiteApp/contact.html", {"form": form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
        
        
def http_test(request):
    return HttpResponse("<h1>Http respond successful</h1>")


def json_test(request):
    return JsonResponse({"test": "success"})
