from django.urls import path
from crmapp import views

urlpatterns = [
    path("", views.home),
]
