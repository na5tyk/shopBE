from django.db import transaction
from core.models import UserRole

def create_default_roles(apps, schema_editor):
    roles = UserRole.ENUMERATE_ROLE_CHOICES

    for user_role in roles:
        with transaction.atomic():
            UserRole.objects.create(name=user_role, index=int(roles[user_role]))

def reverse_create_default_roles(apps, schema_editor):
    UserRole.objects.all().delete()