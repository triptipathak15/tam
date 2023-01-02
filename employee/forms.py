from django.forms import ModelForm, DateInput, ValidationError, Textarea
from .models import LeaveRequest


class DateInput(DateInput):
    input_type = 'date'


class LeaveRequestForm(ModelForm):
    class Meta:
        model = LeaveRequest
        exclude = ['status']
        fields = ['type','comment','start_date','end_date']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
            'comment': Textarea(attrs={'cols': 40, 'rows': 5}),
        }

    def clean(self):
        if self.cleaned_data["start_date"] > self.cleaned_data["end_date"]:
            raise ValidationError("The start date can not be later than end date")
        return self.cleaned_data