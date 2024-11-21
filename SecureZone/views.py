from django.shortcuts import render, get_object_or_404, redirect
from .models import Incident, HelpRequest, SupplyRequest
from .forms import IncidentForm, HelpRequestForm, SupplyRequestForm

def home(request):
    return render(request, 'home.html')

def incident_list(request):
    incidents = Incident.objects.all()
    return render(request, 'incident_list.html', {'incidents': incidents})

def incident_detail(request, pk):
    incident = get_object_or_404(Incident, pk=pk)
    return render(request, 'incident_detail.html', {'incident': incident})

def new_incident(request):
    if request.method == "POST":
        form = IncidentForm(request.POST)
        if form.is_valid():
            incident = form.save(commit=False)
            incident.save()
            return redirect('incident_detail', pk=incident.pk)
    else:
        form = IncidentForm()
    return render(request, 'incident_edit.html', {'form': form})
# In SecureZone/views.py

# In SecureZone/views.py

def supply_request_edit(request):
    helpline_numbers = ["011-26701700", "1-800-621-3362"]
    
    # List of disaster types
    disaster_types = [
        "Earthquake",
        "Flood",
        "Fire",
        "Hurricane",
        "Tornado",
        "Tsunami",
        "Landslide",
        "Volcanic Eruption",
        "Drought",
        "Severe Storm",
        "Pandemic",
        "Chemical Spill",
        "Terrorism"
    ]
    
    guidelines = {
        "earthquake": [
            "Drop to your hands and knees to prevent being knocked over.",
            "Cover your head and neck under a sturdy piece of furniture.",
            "Stay indoors until the shaking stops and you are sure it is safe to exit."
        ],
        "flood": [
            "Move to higher ground and stay there.",
            "Avoid walking or driving through flood waters.",
            "Listen to the radio or TV for information and updates."
        ],
        "fire": [
            "Get out and stay out; do not go back inside for any reason.",
            "Call 911 or your local emergency number.",
            "If you are trapped, signal for help with a flashlight or by waving a cloth."
        ],
        "hurricane": [
            "Evacuate if instructed to do so by local authorities.",
            "Stay indoors and away from windows during the storm.",
            "Have an emergency kit ready with supplies for at least 72 hours."
        ],
        "tornado": [
            "Seek shelter in a sturdy building; avoid windows.",
            "If you are outside or in a mobile home, find a nearby building or ditch.",
            "Cover your head and neck with your arms."
        ],
        "tsunami": [
            "Move to higher ground immediately after an earthquake.",
            "Stay away from the beach and follow evacuation orders.",
            "Be aware of the warning signs such as a rapid rise or fall in coastal waters."
        ],
        "landslide": [
            "Move to higher ground if you live in a landslide-prone area.",
            "Stay away from steep slopes and cliffs during heavy rainfall.",
            "Be alert for signs of a landslide, such as cracking ground or falling rocks."
        ],
        "volcanic eruption": [
            "Follow evacuation orders from local authorities.",
            "Stay indoors and keep windows and doors closed to prevent ash from entering.",
            "Wear masks to protect against ash inhalation."
        ],
        "drought": [
            "Conserve water and use it wisely.",
            "Follow local water restrictions.",
            "Prepare for potential food shortages by growing your own food if possible."
        ],
        "severe storm": [
            "Stay indoors and away from windows.",
            "Listen to weather updates and warnings.",
            "Have an emergency kit ready with food, water, and supplies."
        ],
        "pandemic": [
            "Practice good hygiene, including handwashing and wearing masks.",
            "Follow public health guidelines and stay informed.",
            "Stock up on necessary supplies while avoiding panic buying."
        ],
        "chemical spill": [
            "Evacuate the area if instructed by authorities.",
            "Avoid contact with the chemical and stay upwind.",
            "Report the spill to emergency services immediately."
        ],
        "terrorism": [
            "Be aware of your surroundings and report suspicious activity.",
            "Follow instructions from local authorities during an incident.",
            "Have an emergency plan in place and know your exits."
        ]
    }
    
    return render(request, 'supply_request_edit.html', {
        'helpline_numbers': helpline_numbers,
        'disaster_types': disaster_types,
        'guidelines': guidelines
    })
# Similarly, create views for HelpRequest and SupplyRequest
