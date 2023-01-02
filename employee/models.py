# Create your models here.
from django.db import models
from django.contrib.auth.models import User
REQUEST_STATUSES= (('Submitted','Submitted'),
                   ('Approved','Approved'),
                   ('Denied','Denied'),
                   ('Cancelled','Cancelled'))
REQUEST_TYPES = (('VN','Vacation'),
                 ('SL','Sick Leave'),
                 ('ML','Maternity Leave'),
                 ('BL','Bereavement'),
                 ('CO','Comp. Off'),
                 ('VL','Voluntary Leave'))


class Employee(models.Model):
    employee_id = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    manager = models.ForeignKey(User, on_delete=models.CASCADE, related_name="manager")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE, related_name="leaverequests")
    type = models.CharField(choices=REQUEST_TYPES, max_length=30, default='VN')
    start_date = models.DateField()
    end_date = models.DateField()
    comment = models.TextField(blank=True, null=True)
    status = models.CharField(choices=REQUEST_STATUSES, max_length=30, default='Submitted')

    def __str__(self):
        return str(self.id)