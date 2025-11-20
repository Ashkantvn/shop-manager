from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from products.models import Product
from asgiref.sync import async_to_sync
from products.utils import notify_product_changes

# Dictionary to store old product values before update
_old_values={}

@receiver(pre_save, sender=Product)
def capture_old_values(sender, instance, **kwargs):
    """
    Capture the old values of a product before it's updated.
    This signal runs BEFORE the product is saved to the database.
    """
    if instance.pk: # only capture old values if the instance already exists (update, not create)
        try:
            old_instance = sender.objects.get(pk=instance.pk)
            _old_values[instance.pk]={
                "product_name": old_instance.product_name,
                "quantity": old_instance.quantity,
                "price": old_instance.price,
                "cost_price": old_instance.cost_price,
                "expiry_date": old_instance.expiry_date,
                "supplier_number": old_instance.supplier_number,
            }
        except sender.DoesNotExist:
            _old_values[instance.pk] = None
    else:
        _old_values[instance.pk] = None

@receiver(post_save, sender=Product)
def product_saved(sender, instance, created, **kwargs):
    """
    Send a notification when a product is created or updated.
    This signal runs AFTER the product is saved to the database.
    """
    action = "created" if created else "updated"
    if action == "created":
        # New product was created
        message = f"Product '{instance.product_name}' was created."
        notify_product_changes(message, action)
    else:
        # Existing product was updated - compare old and new values
        old_values = _old_values.get(instance.pk,{})
        changes=[]
        for field,value in old_values.items():
            new_value = getattr(instance, field)
            if new_value != value:
                # Field was changed - add to changes list
                changes.append(f"\n {field}: {value} -> {new_value}")
        if changes:
            message = f"Product '{instance.product_name}' was updated with changes: {''.join(changes)}"
        else:
            message = f"Product '{instance.product_name}' was updated. (no fields changed)"
        notify_product_changes(message, action)


@receiver(post_delete, sender=Product)
def product_deleted(sender, instance, **kwargs):
    """
    Send a notification when a product is deleted.
    This signal runs AFTER the product is deleted from the database.
    """
    message = f"Product '{instance.product_name}' was deleted."
    action = "deleted"
    notify_product_changes(message, action)
