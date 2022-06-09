from django.db import models
from django.urls import reverse

class Airport (models.Model):
	code = models.CharField (max_length=3)
	city = models.CharField (max_length=64)

	def __str__(self):
		return f"{self.city} ({self.code})"

class Flight (models.Model):
	origin = models.ForeignKey (Airport, on_delete=models.CASCADE, related_name='departures')
	destination = models.ForeignKey (Airport, on_delete=models.CASCADE, related_name='arrivals')
	duration = models.IntegerField ()

	def __str__ (self):
		#return (self.origin + " - " + self.destination + " in "+ str(self.duration)+" minutes.")
		#return f"{self.origin} - {self.destination} in {str(self.duration)} minutes"
		return "{} - {} in {} minutes".format (self.origin, self.destination, str(self.duration))

	def get_absolute_url(self):
		return reverse('flights:flight_view', args=[self.id])

class Passenger(models.Model):
	first = models.CharField (max_length=64)
	last = models.CharField (max_length=64)
	flight = models.ManyToManyField (Flight, blank=True, null=True, related_name='passengers')

	def __str__ (self):
		return f"{self.last}, {self.first}"