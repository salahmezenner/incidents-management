from django.shortcuts import redirect , render
from .models import Profile , Incident , Platform , Couche

def incidentList(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role == 'adminapp' or  profile.role == 'superviseur':
        incidents = Incident.objects.all()
        platforms = Platform.objects.all()
        profiles = Profile.objects.filter(role='adminapp')
        context = {'incidents':incidents , 'platforms':platforms , 'profile':profile ,'profiles':profiles}
        return render(request,'incidents/incidents_list.html',context)
    else : 
        return render(request , 'permission.html')

def mesIncident(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role == 'adminapp':
        incidents = Incident.objects.filter(user=user)
        platforms = Platform.objects.all()
        profiles = Profile.objects.all()
        context = {'incidents':incidents , 'platforms':platforms , 'profile':profile ,'profiles':profiles}
        return render(request,'incidents/incidents_list.html',context)
    else : 
        return render(request , 'permission.html')
    

def createIncident(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role == 'adminapp':
        if request.method=='POST':
            intitule = request.POST.get('intitule')
            solution = request.POST.get('solution')
            resume = request.POST.get('resume')
            evaluation = request.POST.get('evaluation')
            nom = request.POST.get('platform')
            technologie = request.POST.get('technologie')
            platform=Platform.objects.get(nom=nom)
            user = request.user
            couche = Couche.objects.get(technologie=technologie)

            incident = Incident.objects.create(intitule=intitule , solution=solution , evaluation=evaluation , platform=platform , user=user, resume=resume , couche=couche) 
            return redirect ('adminapp')
        else :
            platforms=Platform.objects.all()
            couches=Couche.objects.all()
            context={'platforms':platforms , 'couches':couches , 'profile':profile}
            return render(request,'incidents/create_incident.html',context)
    else : 
        return render(request , 'permission.html')

def editIncident(request,incident_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    incident = Incident.objects.get(id=incident_id)
    user_incident = incident.user

    if user == user_incident :
        if request.method=='POST':
            intitule = request.POST.get('intitule')
            resume = request.POST.get('resume')
            solution = request.POST.get('solution')
            evaluation = request.POST.get('evaluation')
            technologie = request.POST.get('technologie')
            nom = request.POST.get('platform')
            platform=Platform.objects.get(nom=nom)
            user = request.user
            couche = Couche.objects.get(technologie=technologie)

            incident.intitule = intitule
            incident.resume = resume
            incident.solution = solution
            incident.evaluation = evaluation 
            incident.platform = platform
            incident.couche = couche

            incident.save()
            return redirect ('adminapp')
        else:
            platforms=Platform.objects.all()
            couches=Couche.objects.all()
            context={'incident':incident , 'couches':couches , 'platforms':platforms , 'profile':profile}
            return render(request,'incidents/create_incident.html',context)
    else : 
        return render(request , 'permission.html')
    
def showIncident(request,incident_id):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role == 'adminapp' or  profile.role == 'superviseur':
        incident = Incident.objects.get(id=incident_id)
        r = []
        for i in range(0,incident.evaluation):
            r.append(i)
        context = {'incident':incident , 'profile':profile , 'r':r}
        return render(request,'incidents/show_incident.html',context)
    else:
        return render(request,'permission.html')