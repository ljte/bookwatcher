from django.urls import path

from . import views

app_name = "authors"

urlpatterns = [
    path("", views.AuthorsListView.as_view(), name="list"),
    path("<int:pk>/about/", views.AuthorAboutView.as_view(), name="about"),
]
