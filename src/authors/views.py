from django.views.generic import DetailView, ListView

from .models import Author


class AuthorsListView(ListView):
    context_object_name = "authors"
    template_name = "authors.html"
    queryset = Author.objects.all()


class AuthorAboutView(DetailView):
    context_object_name = "author"
    template_name = "author.html"
    queryset = Author.objects.prefetch_related("books").all()