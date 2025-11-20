from products import models
from http import HTTPStatus as status
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from datetime import datetime
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

def get_product_or_render_404(request ,product_slug):
    """
    Return product object if found, otherwise render a 404 page.
    """
    try:
        result = get_object_or_404(models.Product, product_slug=product_slug)
        return result, False
    except Http404:
        return render(
            request,
            "404.html",
            {'message': 'Product not found'},
            status= status.NOT_FOUND
        ), True
    
def save_product(request, product=None):
    if product is None:
        product = models.Product()
    fields = [
        "product_name",
        "quantity",
        "price",
        "cost_price",
        "expiry_date",
        "supplier_number",
    ]
    converters = {
        "quantity": int,
        "price": Decimal,
        "cost_price": Decimal,
        "expiry_date": lambda v: datetime.strptime(v, "%Y-%m-%d").date(),
    }
    for field in fields:
        value = request.POST.get(field)
        if value:  # Only update if value is provided and not empty
            if field in converters:
                value = converters[field](value)
            setattr(product, field, value)
    product.save()
    return product

def notify_product_changes(message, action):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "admins",
        {
            "type": "product_change_notification",
            "message": message,
            "action": action,
        }
    )