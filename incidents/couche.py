from django.shortcuts import redirect , render
from .models import Couche , Profile

def list_couches(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='admin':
        couches = Couche.objects.all()

        context = {'couches':couches , 'profile':profile}

        return render(request , 'couches/list_couches.html' , context)
    else:
        return render(request , 'permission.html')
    
def create_couche(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='admin':
        if request.method=='POST':
            couche= request.POST.get('couche')
            technologie = request.POST.get('technologie')

            c = Couche.objects.create(couche=couche , technologie=technologie)

            return redirect('list_couches')
        else:
            context={'profile':profile}
            return render(request , 'couches/create_couche.html' , context)
    else:
        return render(request , 'permission.html')

def edit_couche(request,couche_id):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='admin':
        couche = Couche.objects.get(id=couche_id)
        if request.method=='POST':
            couche.couche= request.POST.get('couche')
            couche.technologie = request.POST.get('technologie')

            couche.save()
            return redirect('list_couches')
        else:
            context={'profile':profile , 'couche':couche}
            return render(request , 'couches/create_couche.html' , context)
    else:
        return render(request , 'permission.html')
    
        
def delete_couche(request,couche_id):
    user = request.user
    profile = Profile.objects.get(user=user)

    if profile.role=='admin':
        couche = Couche.objects.get(id=couche_id)
        couche.delete()
        return redirect('list_couches')
    else:
        return render(request , 'permission.html')