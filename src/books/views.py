
from django.http import HttpResponse, HttpRequest

# Create your views here.


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse(f"Hello, world, you are at {request.path}")
