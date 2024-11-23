from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Relation(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} - Followed - {}'.format(self.from_user, self.to_user)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
