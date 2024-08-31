from django.urls import path
from . import views

urlpatterns = [
    path('normalize_json/', views.normalize_json, name = 'normalize_json'),
]
