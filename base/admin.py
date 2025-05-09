from django.contrib import admin

# Register your models here.
from .models import RoomMember, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created_at")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(RoomMember)
class RoomMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "category", "name", "room_name" , "created_at")
    search_fields = ('name', "room_name")
