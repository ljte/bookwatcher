
from django.http import HttpResponse, HttpRequest
from django.views.generic import DetailView

from .models import Book


# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello, world, you are at {request.path}")


class BookAboutView(DetailView):
    context_object_name = "book"
    template_name = "book.html"
    queryset = Book.objects.select_related("author")
