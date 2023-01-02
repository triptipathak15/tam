"""employee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from employee.views import home, raise_new_request, list_requests, \
    manage_team_requests, change_request_status, loginPage, logoutPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', loginPage),
    path('logout/', logoutPage, name="logout"),
    path('home/', home),
    path('raise', raise_new_request),
    path('list', list_requests),
    path('change_request_status',change_request_status),
    path('manage', manage_team_requests),
    # path("accounts/", include("django.contrib.auth.urls")),
]
