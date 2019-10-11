from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name ='index'),
	path('requestAppointment',views.requestAppointment,name="Request Appointment"),
	path('viewAppointment/<int:appointment_id>/',views.viewAppointment,name="View Appointment"),
	path('cancelAppointment/<int:appointment_id>/',views.cancelAppointment,name="Cancel Appointment "),

]