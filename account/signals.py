"""
Django Signal Handlers for User Profile Creation

This module contains signal handlers that automatically create a Profile
for each new User instance. It leverages Django's `post_save` signal to
trigger the creation of a Profile object whenever a new User is saved to
the database.

Functions:
    create_profile(sender, **kwargs): A signal handler that creates
    a Profile instance whenever a new User is created.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """
    Signal handler that creates a Profile instance for each new User.

    This function is triggered whenever a User instance is saved. It checks
    if the user instance is newly created, and if so, it creates a corresponding
    Profile instance linked to that User.

    Args:
        sender (Model): The model class that sent the signal.
        **kwargs: Additional keyword arguments containing signal information.
            - created (bool): A boolean indicating whether a new record was created.
            - instance (User): The instance of the model being saved.
    """
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])
