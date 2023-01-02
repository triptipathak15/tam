from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LeaveRequestForm
from .models import LeaveRequest, Employee

total = 20


def home(request):
    approved=submitted=declined=cancelled=0
    status_dict = {"Approved":approved,"Submitted":submitted,"Declined":declined,"Cancelled":cancelled}
    id = request.user.id
    requests = LeaveRequest.objects.filter(employee_id=id)
    for item in requests:
        status_dict[item.status]+=1
    return render(request, "home.html", status_dict )


def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home')
        else:
            messages.info(request, "Username/password is incorrect")
    return render(request, "registration/login.html", {})


def logoutPage(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='login')
def raise_new_request(request):
    if request.method == "POST":
        leave_request = LeaveRequestForm(request.POST)
        #
        if leave_request.is_valid():
            emp = Employee.objects.get(id=request.user.id)
            leave_request = LeaveRequest(employee=emp,
                                         start_date=leave_request.cleaned_data["start_date"],
                                         end_date=leave_request.cleaned_data["end_date"])
            leave_request.save()
            messages.success(request, "Leave Request submitted successfully!")
        else:
            messages.error(request, str(leave_request.errors))
    leave_request = LeaveRequestForm()
    return render(request, "raise_new_request.html", {'form': leave_request})


@login_required(login_url='login')
def change_request_status(request):
    request_ids = request.GET['leave_request_ids'].split(',')
    new_status = request.GET['status']
    for request_id in request_ids:
        leave_request = LeaveRequest.objects.get(id=request_id)
        leave_request.status = new_status
        leave_request.save()
    queryset = LeaveRequest.objects.all()
    return render(request, "list_my_requests.html", {'rows': queryset})


@login_required(login_url='login')
def list_requests(request):
    queryset = LeaveRequest.objects.filter(employee__employee_id=request.user.id)
    return render(request, "list_my_requests.html", {'rows': queryset})


@login_required(login_url='login')
def manage_team_requests(request):
    queryset = LeaveRequest.objects.filter(employee__manager_id=request.user.id).\
        exclude(status="Cancelled")
    return render(request, "manage_team_requests.html", {'rows': queryset})