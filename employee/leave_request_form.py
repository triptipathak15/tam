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
        def clean_date(self):
            date = self.cleaned_data['end_date']
            print("***********",date)
            if date < datetime.date.today():
                raise ValidationError("The date cannot be in the past!")
            return date