# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    This signal triggers every time a User is saved.
    If the user is new (created=True), create a profile (only if none exists).
    Otherwise, just save the existing profile to keep it in sync.
    """
    if created:
        # Only create a profile if it doesn't exist
        Profile.objects.get_or_create(user=instance)
    else:
        # If the user already existed, just save the profile
        if hasattr(instance, 'profile'):
            instance.profile.save()
