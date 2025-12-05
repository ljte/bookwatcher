from django.contrib import admin

from .models import Author


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ["fullname", "birthday"]

    @staticmethod
    def fullname(obj: Author) -> str:
        return obj.fullname
