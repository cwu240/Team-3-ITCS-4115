from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from amadeus import Client, ResponseError, Location
from django.http import JsonResponse
amadeus = Client(
    client_id='zO6J8g20wwqn94IxxGMf7ST5ujqPqwGK',
    client_secret='V0PB1OsA5evZA1oq'
)

def select_destination(req, param):
    if req.method == "GET":
        try:
            print(param)
            response = amadeus.reference_data.locations.get(
              keyword=param, subType=Location.ANY) 
            context = {
                "data": response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})

def find_offers(req):
    if req.method == "GET":
        try:
            origin_code = req.GET.get('originCode')
            destination_code = req.GET.get('destinationCode')
            departure_date = req.GET.get('departureDate')
            response = amadeus.shopping.flight_offers_search.get(
                originLocationCode = origin_code,
destinationLocationcode = destination_code,
 departuredate = departure_date, adults=1)
            context = {
                "data" : response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})
             
def price_search(req):
    if req.method == "POST":
        try:
            flight = req.POST.get('flight')
            response = amadeus.shopping.flight_offers.pricing.post(flight)
            print(response.data)
            return JsonResponse
        except ResponseError as error:
            print(error)
    else:
          return JsonResponse({"error": "Invalid request method"})

def book_a_flight(req):
    if req.method == "POST":
        try:
            flight = req.POST.get('flight')
            passenger = req.POST.get('passenger')
            booking = amadeus.booking.flight_orders.post(flight, passenger)
            return JsonResponse(booking)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})
