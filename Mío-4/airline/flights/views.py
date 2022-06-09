from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Flight, Passenger

def home_view (request):
	qs = Flight.objects.all()

	template_name = 'flights/home.html'

	return render (request, template_name, {'flights': qs})

def flight_view (request, fl_id):
	obj = Flight.objects.get(id=fl_id)
	pas = obj.passengers.all()
	non_pas = Passenger.objects.exclude(flight=obj).all()

	template_name = 'flights/flight.html'

	return render (request, template_name, {'flight': obj, 'passengers': pas, 'non_passengers': non_pas})

def flight_book (request, fl_id):
	print (request.method)

	if request.method == 'POST':
		obj = Flight.objects.get(id=fl_id)
		passenger = Passenger.objects.get(id=int(request.POST ['passenger']))
		passenger.flight.add(obj)

		return HttpResponseRedirect (reverse('flights:flight_view', args=(obj.id,)))

	

