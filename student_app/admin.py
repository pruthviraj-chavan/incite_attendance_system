from django.contrib import admin
from .models import StudentProfile, AttendanceRequest, FeeStatus

admin.site.register(StudentProfile)
admin.site.register(AttendanceRequest)
admin.site.register(FeeStatus)
