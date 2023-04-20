from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.contact_us, name="contact_us"),
    path('submit', views.submit, name ="submit_contact_form")

]