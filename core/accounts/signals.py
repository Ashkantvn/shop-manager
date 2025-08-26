from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from accounts.models import CustomUser, BusinessManager

@receiver(post_save, sender=CustomUser)
def create_business_manager(sender, instance, created, **kwargs):
    if created and instance.is_superuser:
        # Automatically create a BusinessManager instance for superusers
        BusinessManager.objects.get_or_create(user=instance)