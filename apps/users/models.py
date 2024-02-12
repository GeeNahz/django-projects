from django.db import models

from django.contrib.auth.models import AbstractUser
from ..utils import DefaultFields
# Create your models here.


class User(DefaultFields, AbstractUser):
    pass
