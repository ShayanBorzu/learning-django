from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, EmailOrUsernameAuthenticationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView  
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = EmailOrUsernameAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username_or_email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successful.")
                return redirect("websiteApp:index")
            else:
                messages.error(request, "Error encountered.")
        else:
            messages.error(request, "Invalid form submission.")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.add_message(request, messages.SUCCESS, "Successful.")
        return redirect("websiteApp:index")
    messages.add_message(request, messages.ERROR, "Error encountered.")
    return redirect("websiteApp:index")


def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Signup successful.")
                return redirect("accounts:login")
            else:
                messages.add_message(request, messages.ERROR, "Error encountered.")
                return redirect("accounts:signup")
    else:
        return redirect("websiteApp:index")
    return render(request, "accounts/signup.html")

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "Email Sent successfully! Please check your inbox.(its in terminal if you are using console backend)"
    success_url = reverse_lazy('accounts:password_reset_done')
    
