from django.urls import path

from . import views


app_name = "app"
urlpatterns = [
	path('',views.IndexView.as_view(), name ='index'),
	path('viewAppointment/<int:pk>/',views.AppointmentView.as_view(),name="View Appointment"),
	path('requestAppointment',views.requestAppointment,name="Request Appointment"),
	path('cancelAppointment/<int:appointment_id>/',views.cancelAppointment,name="Cancel Appointment "),

]