from django.contrib import admin
from .models import User
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "facebook",
        "instagram",
        "telegram",
    )
    search_fields = ("username", "first_name", "last_name")
    list_filter = ("facebook", "instagram", "telegram")
    fieldsets = (
        (
            _("Personal Info"),
            {
                "fields": (
                    "image",
                    "username",
                    "first_name",
                    "last_name",
                    "bio",
                    "password",
                )
            },
        ),
        (_("Social Links"), {"fields": ("facebook", "instagram", "telegram")}),
    )
