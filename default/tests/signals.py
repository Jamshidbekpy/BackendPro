from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save

from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, **kwargs):
    if instance.is_superuser:
        instance.is_staff = True
        
        
@receiver(post_save, sender=User)
def user_post_save(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        instance.is_staff = True
