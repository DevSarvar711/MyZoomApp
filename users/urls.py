from django.urls import path
from .views import (
    CustomLoginView, CustomLogoutView, CustomRegisterView,
    CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView,
    CustomPasswordResetCompleteView, CustomPasswordChangeView, CustomPasswordChangeDoneView
)

app_name = "users"

urlpatterns = [
    # ✅ Foydalanuvchi tizimga kirishi
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", CustomRegisterView.as_view(), name="register"),

    # ✅ Parolni tiklash
    path("password-reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", CustomPasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", CustomPasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password-reset-complete/", CustomPasswordResetCompleteView.as_view(), name="password_reset_complete"),

    # ✅ Parolni o‘zgartirish
    path("password-change/", CustomPasswordChangeView.as_view(), name="password_change"),
    path("password-change/done/", CustomPasswordChangeDoneView.as_view(), name="password_change_done"),
]