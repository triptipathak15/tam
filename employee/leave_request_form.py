import datetime
from django.forms import ModelForm, DateInput, ValidationError
from .models import LeaveRequest


class DateInput(DateInput):
    input_type = 'date'


class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['status']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput()
        }
        def clean_end_date(self):
            start_date = self.cleaned_data['start_date']
            end_date = self.cleaned_data['end_date']
            print("***********",end_date)
            if start_date > end_date:
                raise ValidationError("The start date can not be later than end date")
            return end_date