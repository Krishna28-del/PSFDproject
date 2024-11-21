"""
URL configuration for disasterManagement project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incident_list/', views.incident_list, name='incident_list'),
    path('incident/<int:pk>/', views.incident_detail, name='incident_detail'),
    path('incident/new/', views.new_incident, name='new_incident'),
    path('supply_request_edit/', views.supply_request_edit, name='supply_request_edit'),
    #path('help_request/new/', views.new_help_request, name='new_help_request')
    #path('supply_request/', views.supply_request_list, name='supply_request_list'),
    #path('help_request/', views.help_request_list, name='help_request_list'),
    # Add paths for HelpRequest and SupplyRequest views
]
