from datetime import datetime

from django.db import models

from authors.shared import Author


class Book(models.Model):
    title: str = models.TextField()
    isbn: int = models.IntegerField(unique=True, db_index=True, null=True, blank=True)
    description: str = models.TextField(null=True)
    finished_at: datetime = models.DateTimeField(null=True, blank=True)

    author: Author = models.ForeignKey(
        Author,
        related_name="books",
        on_delete=models.PROTECT,
    )

    objects = models.Manager()

    class Meta:
        db_table = "book"
