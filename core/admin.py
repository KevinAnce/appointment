from django.contrib import admin

from core.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    pass