import uuid

from django.conf import settings
from django.db import models
from django.db.models import SET_NULL


class FileUpload(models.Model):

    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    md5 = models.CharField(max_length=32, blank=True, null=True)
    file = models.FileField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        editable=False,
        on_delete=SET_NULL
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.file.name}'

    @property
    def url(self):
        return self.file.url
