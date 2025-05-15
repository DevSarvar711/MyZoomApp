from django.contrib.auth import login, logout
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.views import (
    LoginView, PasswordResetView, PasswordResetDoneView,
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
)
from django.views import View
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from .forms import (
    CustomLoginForm, CustomUserCreationForm, CustomPasswordResetForm, CustomSetPasswordForm,
    CustomPasswordChangeForm, UserProfileForm
)
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404


# ✅ **Foydalanuvchi tizimga kirishi**
class CustomLoginView(LoginView):
    template_name = "users/login.html"
    authentication_form = CustomLoginForm

    def get_success_url(self):
        return reverse_lazy("videochat:home_url")


# ✅ **Tizimdan chiqish**
class CustomLogoutView(View):
    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
            return redirect("users:login")  # Login sahifasiga yo‘naltiramiz
        return HttpResponseForbidden("You are not allowed to perform this action.")



# ✅ **Ro‘yxatdan o‘tish (register)**
class CustomRegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("videochat:home_url")


# ✅ **Parolni tiklash (reset qilish)**
class CustomPasswordResetView(PasswordResetView):
    template_name = "users/password_reset.html"
    email_template_name = "users/password_reset_email.html"
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy("users:password_reset_done")


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = "users/password_reset_done.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    form_class = CustomSetPasswordForm
    success_url = reverse_lazy("users:password_reset_complete")


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "users/password_reset_complete.html"


# ✅ **Parolni o‘zgartirish (login bo‘lgan foydalanuvchi)**
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_change.html"
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = "users/password_change_done.html"




