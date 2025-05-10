from django.db import models
from shared.utility import valid_image_types
from django.core.validators import FileExtensionValidator
# Create your models here.

class Category(models.Model):
    logo = models.ImageField(
        upload_to="category-pictures/",
        validators=[FileExtensionValidator(allowed_extensions=valid_image_types)],
        default="user-pictures/default-category-picture.jpg"
    )
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class RoomMember(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="rooms", null=True, blank=True)
    name = models.CharField(max_length=200)
    uid = models.CharField(max_length=200)
    room_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        
