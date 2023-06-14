import uuid

from django.db.models import Model, UUIDField, DateTimeField


class BaseModel(Model):
    id = UUIDField(unique=True, default=uuid.uuid4, editable=False, primary_key=True)
    created_time = DateTimeField(auto_now_add=True)
    updated_time = DateTimeField(auto_now=True)

    class Meta:
        abstract = True
