from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    # user = models.OneToOneField(User)
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
