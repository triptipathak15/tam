from django.forms import ModelForm
from .models import LeaveRequest


class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['status']