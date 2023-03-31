from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from amadeus import Client, ResponseError, Location
from django.http import JsonResponse
amadeus = Client(
    client_id='GSGkZkcWo4V0xWdbw9ZA2KlbHA94PqfL',
    client_secret='6k4W8AU73P0XOA78'
)

def select_destination(req, param):
    if req.method == "GET":
        try:
            response = amadeus.reference_data.locations.get(keyword=param, subType=Location.ANY) 
            
            context = {
                "data": response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print("ayo")
            print(error)

    else:
        return JsonResponse({"error": "Invalid request method"})

def search_offers(req):
    if req.method == "GET":
        try:
            origin_code = req.GET.get('originCode')
            destination_code = req.GET.get('destinationCode')
            departure_date = req.GET.get('departureDate')
            print('origin code: ', origin_code)
            print('destination code: ', destination_code)
            print('departur data: ',departure_date)
            response = amadeus.shopping.flight_offers_search.get(originLocationCode = origin_code,destinationLocationCode = destination_code, departureDate = departure_date, adults=1)
            context = {
                "data" : response.data
            }
            return JsonResponse(context)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})

@csrf_exempt         
def price_search(req):
    if req.method == "POST":
        try:
            data = json.loads(req.body)
            flight = data.get("flight")
            response = amadeus.shopping.flight_offers.pricing.post(flight)
            print(response.data)
            return JsonResponse
        except ResponseError as error:
            print(error)
    else:
          return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def book_a_flight(req):
    if req.method == "POST":
        try:
            data = json.loads(req.body)
            flight = data.get("flight")
            passenger = req.POST.get('passenger')
            booking = amadeus.booking.flight_orders.post(flight, passenger)
            return JsonResponse(booking)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})
