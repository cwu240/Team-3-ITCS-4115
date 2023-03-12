from django.shortcuts import render

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