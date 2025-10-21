from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def login_view(request):
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("websiteApp:index")
            else:
                return render(request, "accounts/login.html", {"error": "Invalid username or password."})
        return render(request, "accounts/login.html")
def logout_view(request):
    if request.user.is_authenticated:
        return render(request, "accounts/logout.html")  
    return render(request, "accounts/notverified.html")

def signup_view(request):
    return render(request, "accounts/signup.html")