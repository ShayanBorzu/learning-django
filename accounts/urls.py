from django.urls import path
from accounts.views import login_view, logout_view, signup_view, ResetPasswordView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "accounts"


urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
    # 1. Request form
    path(
        "password-reset/",
        ResetPasswordView.as_view(),
        name="password_reset"
    ),

    # 2. Email-sent confirmation
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="accounts/password_reset_done.html"
        ),
        name="password_reset_done"
    ),

    # 3. Reset-link confirm — **FIXED** placeholders here
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url = reverse_lazy("accounts:password_reset_complete")
        ),
        name="password_reset_confirm",
    ),

    # 4. Reset complete
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html"
        ),
        name="password_reset_complete"
    ),
]