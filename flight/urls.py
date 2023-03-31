from django.urls import path, include
from . import views

urlpatterns = [
    path('select_destination/<str:param>', views.select_destination,name="select_destination"),
    path('search_offers/', views.search_offers, name="search_offers"),
    path('price_search/', views.price_search, name="price_search"),
    path('book_a_flight/', views.book_a_flight, name="book_a_flight"),
    path("accounts/", include("django.contrib.auth.urls")),
]