from django.shortcuts import render,HttpResponse,Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from datetime import datetime

from .models import AppointmentRequest,Institution
# Create your views here.


class IndexView(generic.ListView):
	"""docstring for IndexView"""
	template_name = 'app/index.html'
	context_object_name = 'institutions'

	def get_queryset(self):
		return Institution.objects.all()
	pass

class AppointmentView(generic.DetailView):
	"""docstring for DetailView"""
	model = AppointmentRequest
	template_name = 'app/appointment_view.html'
	
def requestAppointment(request):
	try:
		req = AppointmentRequest(reason=request.POST["reason"],dateReserved=datetime.strptime(request.POST["date"], "%Y-%m-%d"),institution=Institution.objects.get(pk=request.POST["institution"]));
		req.save();
	except Institution.DoesNotExist:
		raise Http404("Can Not find Institution with Id of {}".format(request.POST["institution"]))
	return HttpResponse("requestAppoiment");


def cancelAppointment(request,appointment_id):
	return HttpResponse("Canceled Appoiment")