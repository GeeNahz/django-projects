import uuid
from django_extensions.db.models import TimeStampedModel
from django.db import models


class DefaultFields(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, db_index=True, editable=False, default=uuid.uuid4)

    class Meta:
        abstract = True
