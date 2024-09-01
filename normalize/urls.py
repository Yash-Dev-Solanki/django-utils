from django.urls import path
from . import views

urlpatterns = [
    path("", views.normalize_json, name = 'normalize_json'),
]
