from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from products.models import Product
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@receiver(post_save, sender=Product)
def product_created(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "dashboard",
            {
                "type": "product_created",
                "message": f"{instance} created"
            }
        )

@receiver(pre_save, sender=Product)
def product_updated(sender, instance, **kwargs):
    
    try:
        old_instance = sender.objects.get(pk=instance.pk)
    except sender.DoesNotExist:
        return
    

    changes = {}
    for field in instance._meta.fields:
        field_name = field.name
        old_value = getattr(old_instance, field_name)
        new_value = getattr(instance, field_name)
        if old_value != new_value:
            changes[field_name] = {
                "old_value": old_value,
                "new_value": new_value,
            }

    if changes:
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'dashboard',
            {
                'type': "product_updated",
                'product': str(instance),
                "message": changes
            }
        )