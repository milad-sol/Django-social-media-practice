"""
Django Models for User Profile and Relationships

This module defines the models used for the user profile and user relationships
within the application. The `Profile` model extends the user model with additional
attributes, while the `Relation` model represents user-to-user follow relationships.

Classes:
    Relation(models.Model): Model representing a follow relationship between users.
    Profile(models.Model): Model representing additional user profile information.
"""

from django.contrib.auth.models import User
from django.db import models


class Relation(models.Model):
    """
    Model representing a follow relationship between users.

    This model creates a directional relationship between two `User` instances
    to represent a following relationship. For example, if `from_user` follows
    `to_user`, it indicates that `from_user` is a follower of `to_user`.

    Attributes:
        from_user (ForeignKey): The user who is following another user.
        to_user (ForeignKey): The user being followed.
        created (DateTimeField): The timestamp when the follow relationship was created.
    """
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - Followed - {}'.format(self.from_user, self.to_user)


class Profile(models.Model):
    """
    Model representing additional user profile information.

    This model extends the built-in `User` model by adding more attributes
    related to user profile such as age and bio.

    Attributes:
        user (OneToOneField): One-to-one relationship with the `User` model.
        age (PositiveIntegerField): The age of the user.
        bio (TextField): A short biography of the user.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
