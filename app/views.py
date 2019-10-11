from django.shortcuts import render,HttpResponse,Http404
from django.template import loader
from datetime import datetime

from .models import AppointmentRequest,Institution
# Create your views here.

def index(request):

	return render(request,'app/index.html',{'institutions':Institution.objects.all()})

def requestAppointment(request):
	print(request.POST["date"])
	try:
		req = AppointmentRequest(reason=request.POST["reason"],dateReserved=datetime.strptime(request.POST["date"], "%Y-%m-%d"),institution=Institution.objects.get(pk=request.POST["institution"]));
		print(req)
		req.save();
	except Institution.DoesNotExist:
		raise Http404("Can Not find Institution with Id of {}".format(request.POST["institution"]))
	return HttpResponse("requestAppoiment");

def viewAppointment(request,appointment_id):
	try:
		appointment_request = AppointmentRequest.objects.get(pk=appointment_id);
	except Appoiment.DoesNotExist:
		raise Http404("Appoiment Does Not Exist")
	return render(request,'app/appointment_view.html',{"appointment_request":appointment_request})

def cancelAppointment(request,appointment_id):
	return HttpResponse("Canceled Appoiment")