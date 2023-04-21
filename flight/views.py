from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Tickets
from django.contrib import messages

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
            print("flight \n ", flight)
            response = amadeus.shopping.flight_offers.pricing.post(flight)
            return JsonResponse(response.data)
        except ResponseError as error:
            print(error)
    else:
          return JsonResponse({"error": "Invalid request method"})

@csrf_exempt
def book_a_flight(req):
    if req.method == "POST":
        current_user = req.user
        try:
            data = json.loads(req.body)
            print(data)
            flight = data.get("flight")
            print("flight" , flight)
            passenger = data.get('traveler')
            print(passenger)
            
            traveler = {
                'id': '1',
                'dateOfBirth': str(current_user.dob),
                'name': {
                    'firstName': current_user.first_name,
                    'lastName': current_user.last_name
                },
                'gender': 'MALE',
                'contact': {
                    'emailAddress': current_user.email,
                    'phones': [{
                        'deviceType': 'MOBILE',
                        'countryCallingCode': '1',
                        'number': current_user.phone_number
                    }]
                },
                'documents': [{
                    'documentType': 'PASSPORT',
                    'birthPlace': 'Madrid',
                    'issuanceLocation': 'Madrid',
                    'issuanceDate': '2015-04-14',
                    'number': '00000000',
                    'expiryDate': '2025-04-14',
                    'issuanceCountry': 'ES',
                    'validityCountry': 'ES',
                    'nationality': 'ES',
                    'holder': True
                }]
            }


            try:
                #TODO --- instead of below line, just store ticket for flight in database
                booking = amadeus.booking.flight_orders.post(flight, traveler).data
                ticket_obj = Tickets.objects.create(customer_id = current_user, json_ticket_data = booking)
                ticket_obj.save()
                messages.success(req, 'your flight has been booked')
            except Exception as error:
                print("erorr when booking")
                print(error)

            return JsonResponse(booking)
        except ResponseError as error:
            print(error)
    else:
        return JsonResponse({"error": "Invalid request method"})
