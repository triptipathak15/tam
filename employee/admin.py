from django.contrib import admin
from .models import Employee, LeaveRequest


class LeaveRequestAdmin(admin.ModelAdmin):
    exclude = ('status',)


admin.site.register(Employee)
admin.site.register(LeaveRequest, LeaveRequestAdmin)
