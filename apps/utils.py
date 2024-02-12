import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class DefaultFields(TimeStampedModel, models.Model):
    id = models.UUIDField(
        db_index=True,
        primary_key=True,
        unique=True,
        null=False,
        blank=False,
        editable=False,
        default=uuid.uuid4,
    )

    class Meta:
        abstract = True
