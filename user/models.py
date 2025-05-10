from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    ADMIN = ('admin','Admin')
    WRITER = ('writer','Writer')
    READER=('reader','Reader')

class CustomUser(AbstractUser):
    role=models.CharField(max_length=20,choices=Role,default=Role.READER)