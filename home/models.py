from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return '{} - {}'.format(self.pk, self.user)

    def get_absolute_url(self):
        return reverse('home:post_detail', kwargs={'pk': self.pk, 'slug': self.slug})
