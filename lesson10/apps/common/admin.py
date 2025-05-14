from django.contrib import admin
from .models import ContactUs
from django.utils.translation import gettext_lazy as _


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "short_message")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = (
        "name",
        "email",
        "subject",
        "message",
    )  # foydalanuvchi yozgan narsani faqat ko‘rish

    def short_message(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

    short_message.short_description = _("Message preview")
