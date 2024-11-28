from django.core.management.base import BaseCommand
from django.utils.timezone import now
from core.models import *

class Command(BaseCommand):
    help = "Delete unverified users older than two days"

    def handle(self, *args, **kwargs):
        unverified_users = CustomUser.objects.filter(is_verified=False, verification_expiry__lte=now())
        count = unverified_users.count()
        unverified_users.delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} unverified users."))
