from celery import shared_task
from accounts.models import AccessTokenBlackList
from django.utils import timezone
from datetime import timedelta


@shared_task
def delete_expired_token():
    """
    Task to delete expired access tokens from the blacklist.
    """
    cutoff = timezone.now() - timedelta(minutes=5)
    for token in AccessTokenBlackList.objects.all():
        if token.created_date < cutoff:
            token.delete()
    return "Expired tokens deleted successfully"