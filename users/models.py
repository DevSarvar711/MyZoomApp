from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, MaxLengthValidator
from django.db import models
from shared.models import BaseModel
from shared.utility import valid_image_types
from django.utils.translation import gettext_lazy as _



class CustomUser(BaseModel, AbstractUser):
    birthday = models.DateField(_("Birthday"), null=True, blank=True, help_text=_("User's date of birth"))
    interest = models.CharField(_("Interest"), max_length=250, null=True, blank=True)
    picture = models.ImageField(
        _("Profile Picture"),
        upload_to="user-pictures/",
        validators=[FileExtensionValidator(allowed_extensions=valid_image_types)],
        default="user-pictures/default-profile-picture.jpg"
    )
    website = models.URLField(_("Website"), null=True, blank=True)
    bio = models.TextField(_("Bio"), null=True, blank=True, validators=[MaxLengthValidator(5000)])


    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["last_name", "first_name"]

    @property
    def full_name(self):
        return " ".join(filter(None, [self.first_name, self.last_name]))

    def __str__(self):
        return f"{self.username}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) 