from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_tickets, name="view_tickets"),

]