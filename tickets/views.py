from django.shortcuts import render

# Create your views here.
def view_tickets(request):
   return render(request, "tickets/tickets.html", {})