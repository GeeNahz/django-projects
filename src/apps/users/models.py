from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from apps.utils import DefaultFields


class User(DefaultFields, AbstractUser):
    pass


class Speaker(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='speaker_profile', null=True
    )
    bio = models.TextField(_('Speaker bio'), blank=True)
    website = models.URLField(null=True, blank=True)
    company = models.CharField(max_length=200, blank=True)
