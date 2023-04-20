# accounts/urls.py
from django.urls import path

from .views import SignUpView
from .views import profile_page
from .views import submit


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile_page/", profile_page, name="profile_page"),
    path('profile_page/submit', submit, name ="submit_profile_form")
]