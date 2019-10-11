from django.contrib import admin

# Register your models here.

from .models import AppointmentRequest

admin.site.register(AppointmentRequest)
