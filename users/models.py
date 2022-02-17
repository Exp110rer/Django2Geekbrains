from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.timezone import now
from datetime import timedelta


def activation_key_expiration_date():
    return now() + timedelta(hours=48)


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', blank=True)
    activation_key = models.CharField(max_length=256, blank=True)
    activation_key_expires = models.DateTimeField(default=activation_key_expiration_date)

    def is_activation_key_expired(self):
        return False if now() <= self.activation_key_expires else True
