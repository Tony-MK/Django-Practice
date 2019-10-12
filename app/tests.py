from django.test import TestCase
from django.utils import timezone

# Create your tests here.

from .models import AppointmentRequest,Institution
from datetime import timedelta

class AppointmentRequestTets(TestCase):

	def test_appointment_request(self):
		"Booking an appointment 30 days in the past"
		try:
			AppointmentRequest(
				reason="Headache",
				dateReserved=timezone.now() - timedelta(days=30)
			);
		except:
			self.assertIs(False,False);
		self.assertIs(True,False);



