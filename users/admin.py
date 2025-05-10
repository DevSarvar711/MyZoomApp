from django.contrib import admin
from django.utils.safestring import mark_safe
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):

    list_display = (
        "id", "full_name", "email",
        "picture_preview", "is_active", "is_staff", "date_joined"
    )
    list_display_links = ("full_name", "email")
    search_fields = ("first_name", "last_name", "email")
    list_filter = ("is_active", "is_staff", "date_joined")
    ordering = ("last_name", "first_name")

    readonly_fields = ("picture_preview", "date_joined", "last_login")
    fieldsets = (
        ("Personal Information", {
            "fields": ("first_name", "last_name", "birthday", "picture", "picture_preview")
        }),
        ("Contact Information", {
            "fields": ("email", "website",)
        }),
        ("Additional Details", {
            "fields": ("bio", "interest")
        }),
        ("Permissions & Roles", {
            "fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
        }),
        ("Important Dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        ("Create New User", {
            "classes": ("wide",),
            "fields": ("first_name", "last_name", "email", "password1", "password2", "is_active", "is_staff"),
        }),
    )

    def picture_preview(self, obj):
        if obj.picture:
            return mark_safe(f'<img src="{obj.picture.url}" width="60" height="auto" style="border-radius: 5px;">')
        return "No Image"

    picture_preview.short_description = "Profile Picture"

    def full_name(self, obj):
        return obj.full_name

    full_name.short_description = "Full Name"