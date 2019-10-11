from django.db import models

# Create your models here.


class Institution(models.Model):
	"""docstring for Institution"""
	name = models.CharField(max_length=200);
	location = models.CharField(max_length=200);
	rating = models.FloatField(max_length=200)
	email = models.EmailField(max_length=254);

	def __str__(self):
		return '{} Located: {} Rating: {} Email: {}'.format(self.name,self.location,self.rating,self.email);
		

class AppointmentRequest(models.Model):
	"""docstring for AppointmentRequest"""
	reason = models.CharField(max_length=1000);
	dateReserved = models.DateTimeField('Date Booked');
	institution = models.ForeignKey(Institution,on_delete=models.DO_NOTHING)

	def __str__(self):
		return 'Reason: {} Date: {} Institution: ({})'.format(self.reason,self.dateReserved,self.institution.name);