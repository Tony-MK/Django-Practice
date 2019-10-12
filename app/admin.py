from django.contrib import admin

# Register your models here.

from .models import AppointmentRequest,Institution

admin.site.register(AppointmentRequest);
admin.site.register(Institution);