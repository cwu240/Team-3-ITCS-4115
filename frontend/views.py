from django.shortcuts import render

# Create your views here.
def Booking(req):
    return render(req, 'booking.html')

