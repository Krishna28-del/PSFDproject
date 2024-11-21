from django import forms
from .models import Incident, HelpRequest, SupplyRequest

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location']

class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ['incident', 'description']

class SupplyRequestForm(forms.ModelForm):
    class Meta:
        model = SupplyRequest
        fields = ['supplies_needed', 'quantity']