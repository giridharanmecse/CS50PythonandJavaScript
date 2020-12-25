from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dharani", views.dharani, name="dharani"),
    path("giri", views.giri, name="giri"),
    path("<str:name>", views.greet, name = "greet")
]