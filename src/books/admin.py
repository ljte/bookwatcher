from django.contrib import admin

from .models import Book


# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "isbn", "author_fullname"]

    @staticmethod
    def author_fullname(obj: Book) -> str:
        return getattr(obj.author, "fullname", "<fullname>")