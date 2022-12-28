from django.contrib import messages
from django.shortcuts import render
from .leave_request_form import LeaveRequestForm
from .models import LeaveRequest


def home(request):
    return render(request, "base.html")


def raise_new_request(request):
    if request.method == "POST":
        leave_request = LeaveRequestForm(request.POST)
        if leave_request.is_valid():
            messages.success(request, "Leave Request submitted successfully!")
            leave_request.save()
    leave_request = LeaveRequestForm()
    return render(request, "raise_new_request.html", {'form': leave_request})


def change_request_status(request):
    request_ids = request.GET['leave_request_ids'].split(',')
    new_status = request.GET['status']
    for request_id in request_ids:
        leave_request = LeaveRequest.objects.get(id=int(request_id))
        leave_request.status = new_status
        leave_request.save()
    queryset = LeaveRequest.objects.all()
    return render(request, "list_my_requests.html", {'rows': queryset})



def list_requests(request):
    id = 1
    queryset = LeaveRequest.objects.all()
    return render(request, "list_my_requests.html", {'rows': queryset})


def manage_team_requests(request):
    id = 1
    queryset = LeaveRequest.objects.all()
    return render(request, "manage_team_requests.html", {'rows': queryset})