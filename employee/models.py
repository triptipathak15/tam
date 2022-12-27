# Create your models here.
from django.db import models

REQUEST_STATUSES= (('Submitted','Submitted'),
                   ('Approved','Approved'),
                   ('Cancelled','Cancelled'))
REQUEST_TYPES = (('VN','Vacation'),
                 ('SL','Sick Leave'),
                 ('ML','Maternity Leave'),
                 ('BL','Bereavement Leave'),
                 ('CO','Compensation Off'),
                 ('VL','Voluntary Leave'))


class Employee(models.Model):
    employee_id = models.IntegerField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    manager_employee_id = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.employee_id}-{self.first_name} {self.last_name}"


class LeaveRequest(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    type = models.CharField(choices=REQUEST_TYPES, max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=REQUEST_STATUSES, max_length=30, default='Submitted')

    def __str__(self):
        return f"{self.employee.first_name} - {self.type} from {self.start_date} to " \
               f"{self.end_date}"
