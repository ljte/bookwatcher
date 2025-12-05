from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/about/", views.BookAboutView.as_view(), name="about"),
]
