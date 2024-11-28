from celery import shared_task
from django.utils.timezone import now
from core.models import *

@shared_task
def delete_unverified_users():
    """
    Deletes unverified users whose verification_expiry has passed.
    """
    unverified_users = CustomUser.objects.filter(is_verified=False, verification_expiry__lte=now())
    count = unverified_users.count()
    unverified_users.delete()
    return f"Deleted {count} unverified users."
