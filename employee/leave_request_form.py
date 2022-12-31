import datetime
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, DateInput, ValidationError, Textarea
from django.db import models
from django.db.models import F,Q, CheckConstraint
from .models import LeaveRequest


class DateInput(DateInput):
    input_type = 'date'


class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['status']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'comment': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

    def clean(self):
        if self.cleaned_data["start_date"] > self.cleaned_data["end_date"]:
            raise ValidationError("The start date can not be later than end date")
        return self.cleaned_data