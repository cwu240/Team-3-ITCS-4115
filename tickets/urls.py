from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.view_tickets, name="view_tickets"),
    path(r'tickets/(?P<pk>[0-9]+)/$', views.ticket_delete, name='ticket_delete')

]