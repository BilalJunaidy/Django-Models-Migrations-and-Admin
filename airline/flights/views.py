from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Flight, Airport 

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all(),
        "airports": Airport.objects.all()
    })

def flight(request, flight_id):

    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight": flight, 
        "passengers": passengers
    })

def book(requet, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk = int(request.POST["passenger"]))
        passenger.flights.add(flight)

        return HttpResponseRedirect(reverse("flight", args=(flight.id)))

    else:
        return render(request, "flights\book.html")
