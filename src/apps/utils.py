import uuid
from django.db import models
from django_extensions.db.models import TimeStampedModel


class DefaultFields(TimeStampedModel, models.Model):
    id = models.UUIDField(
        primary_key=True, unique=True, editable=False, default=uuid.uuid4, db_index=True
    )

    class Meta:
        abstract = True
