from django.contrib import messages
from django.shortcuts import render
from .leave_request_form import LeaveRequestForm


def index(request):
    if request.method == "POST":
        leave_request = LeaveRequestForm(request.POST)
        if leave_request.is_valid():
            leave_request.save()
            messages.success(request, "Leave Request submitted successfully!")
    leave_request = LeaveRequestForm()
    return render(request, "leave_request.html", {'form': leave_request})