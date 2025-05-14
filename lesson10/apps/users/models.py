from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    image = models.ImageField(
        _("Profile image"), upload_to="users/", blank=True, null=True
    )
    bio = models.CharField(_("Biography"), max_length=255, blank=True)
    username = models.CharField(_("Username"), max_length=150, unique=True)
    first_name = models.CharField(_("First name"), max_length=100)
    last_name = models.CharField(_("Last name"), max_length=100)
    facebook = models.URLField(_("Facebook link"), blank=True, null=True)
    instagram = models.URLField(_("Instagram link"), blank=True, null=True)
    telegram = models.URLField(_("Telegram link"), blank=True, null=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username
