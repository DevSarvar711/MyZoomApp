from django.urls import path
from . import views

app_name = "videochat"  # URL nomlarini `videochat:lobby_url` tarzida ishlatish uchun

urlpatterns = [
    path('', views.Home, name="home_url"),
    path('lobby/', views.lobby, name="lobby_url"),
    path('room/', views.room, name="room_url"),

    # Token va a'zolik endpointlari
    path('get_token/', views.getToken, name="get_token"),
    path('create_member/', views.createMember, name="create_member"),
    path('get_member/', views.getMember, name="get_member"),
    path('delete_member/', views.deleteMember, name="delete_member"),
]
