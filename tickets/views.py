from django.shortcuts import render
from django.apps import apps
import json 
import ast

# Create your views here.
def view_tickets(request):
   Tickets = apps.get_model('flight', 'Tickets')

   ticket_list = list(Tickets.objects.filter(customer_id=request.user))


   for i in range(0, len(ticket_list)):
      ticket_list[i] = ast.literal_eval(str(ticket_list[i].json_ticket_data))

   tickets_list_short = []
   for i in range(0, len(ticket_list)):

      dicti = {}

      #print(type(ticket_list[i]))
      #print("\n")
      #print(ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'] )
      #print(ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][0]['departure']['iataCode'] )
      #print(ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][-1]['arrival']['iataCode'] )

      dicti['dept_iata'] = ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][0]['departure']['iataCode']
      dept_time = ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][0]['departure']['at'].replace('T',' ').split(' ')
      dicti['dept_date'] = dept_time[0]
      dicti['dept_time'] = dept_time[1]
      dicti['arr_iata'] = ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][-1]['arrival']['iataCode']
      arr_time = ticket_list[i]['flightOffers'][0]['itineraries'][0]['segments'][-1]['arrival']['at'].replace('T',' ').split(' ')
      dicti['arr_date'] = arr_time[0]
      dicti['arr_time'] = arr_time[1]
      tickets_list_short.append(dicti)


      #print("\n")
      #print("\n")
      #print("\n")
      



   return render(request, "tickets/tickets.html", {'tickets':ticket_list ,'short_list':tickets_list_short})