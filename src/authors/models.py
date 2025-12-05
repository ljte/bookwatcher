from datetime import datetime

from django.db import models


class Author(models.Model):
    first_name: str = models.CharField()
    second_name: str = models.CharField()
    birthday: datetime = models.DateTimeField(null=True, blank=True)
    description: str = models.TextField(null=True, blank=True)

    objects = models.Manager()

    class Meta:
        db_table = "author"

    @property
    def fullname(self) -> str:
        return f"{self.first_name} {self.second_name}"
