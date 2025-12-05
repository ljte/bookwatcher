from datetime import datetime

from django.db import models


class Author(models.Model):
    first_name: str = models.CharField()
    second_name: str = models.CharField()
    birthday: datetime = models.DateTimeField(null=True, blank=True)
    description: str = models.TextField(null=True, blank=True)

    class Meta:
        table_name = "author"

