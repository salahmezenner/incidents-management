from django.shortcuts import render , redirect
from .models import Profile , Incident , Platform
from django.db.models import Count
from django.db.models.functions import ExtractMonth

def stat_per_platforms(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='adminapp' or profile.role=='superviseur':
        platforms = Incident.objects.values('platform').annotate(counting=Count('id'))
        arr=[]
        for p in platforms:
            platform_id= p.get('platform')
            platform = Platform.objects.get(id=platform_id)
            counting = p.get('counting')

            arr.append({'platform':platform , 'counting':counting})

        context = {'platforms':arr}
        return render(request ,'stat_per_platforms.html',context)
    else:
        return render(request,'permission.html')
    
def stat_per_year(request,year):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='adminapp' or profile.role=='superviseur':
        incidents_year = Incident.objects.filter(datetime__year=year).annotate(month=ExtractMonth('datetime')).values('month').annotate(counting=Count('id'))
        incidents=[]
        for i in incidents_year:
            month = i.get('month')
            counting = i.get('counting')

            incidents.append({'month':month , 'counting':counting})
        context={'incidents':incidents}

        return render(request , 'stat_per_year.html' , context)
    else:
        return render(request,'permission.html')
    
