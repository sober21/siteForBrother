from django.urls import path
from . import views

app_name = "simplesite"
urlpatterns = [
    path("", views.index, name="index"),
    path("second/", views.second, name="second")
]
