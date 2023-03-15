from django.urls import path, include
from . import views

urlpatterns = [
    path('select_destination/<str:param>', views.select_destination,name="select_destination"),
    path("accounts/", include("django.contrib.auth.urls")),
]