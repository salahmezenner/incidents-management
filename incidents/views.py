from django.shortcuts import render
from .login import loginView , logoutView
from .models import Profile
from .adminapp import incidentList , mesIncident  , createIncident , editIncident , showIncident
from .superadmin import superadmin_dashbord,signup_view , user_list , user_delete , user_edit
from .superadmin import platform_create , platform_delete , platform_edit , platform_list 
from .cellule_de_crise import envoi_mail , add_event , cellule_view , delete_event
from .statestique import stat_per_platforms , stat_per_year
from .couche import list_couches , create_couche , edit_couche , delete_couche
from django.http import JsonResponse

from .models import Incident,Platform
import calendar
import json
import logging


def adminapp(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='adminapp':
        return render(request,'adminapp.html')

def superadmin(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='superadmin':
        return render(request,'superadmin.html')

def dashboard(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='adminapp' or profile.role=='superviseur':
        context = {'profile' : profile}
        return render(request, 'incidents/dashboard.html',context)

# gettingg incidentsdata
logger = logging.getLogger(__name__)
def get_incidents_data(request):
    year = request.GET.get('year')
    if not year:
        logger.error('Year parameter is required.')
        return JsonResponse({'error': 'Year parameter is required.'}, status=400)
    
    try:
        year = int(year)
    except ValueError:
        logger.error('Year parameter must be an integer.')
        return JsonResponse({'error': 'Year parameter must be an integer.'}, status=400)

    try:
        incidents = Incident.objects.filter(datetime__year=year)
        monthly_data = {str(month): incidents.filter(datetime__month=month).count() for month in range(1, 13)}
        yearly_total = incidents.count()
    except Exception as e:
        logger.exception('An error occurred while fetching incidents data.')
        return JsonResponse({'error': 'An error occurred while fetching incidents data.'}, status=500)

    data = {
        'monthlyData': monthly_data,
        'yearlyTotal': yearly_total
    }

    return JsonResponse(data)




def platform_chart(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='adminapp' or profile.role=='superviseur':
        if request.method == 'GET' and 'json' in request.GET:
            platform_names = []
            incident_counts = []

            platforms = Platform.objects.all()
            for platform in platforms:
                incidents = Incident.objects.filter(platform=platform)
                platform_names.append(platform.nom)
                incident_counts.append(incidents.count())

            return JsonResponse({'platform_names': platform_names, 'incident_counts': incident_counts})
        else:
            context = {'profile' : profile}
            return render(request, 'incidents/charte.html',context)