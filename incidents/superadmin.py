from django.shortcuts import redirect,render
from .models import Profile,User,Platform
import re

def superadmin_dashbord(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        context={'profile':profile}
        return render(request,'superadmin/superadmin.html',context)
    else:
        return render(request , 'permission.html')
    

def signup_view(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        erreur=False
        if request.method=='POST':
            fullname = request.POST.get('fullname')
            username = request.POST.get('username')
            role = request.POST.get('role')
            email = request.POST.get('email')           
            password = request.POST.get('password')

            if len(password)<8 :
                erreur=True
                context={'erreur':erreur}
                return render(request , 'users/create_user.html' , context)
            
            if not re.search(r'[A-Z]',password):
                erreur=True
                context={'erreur':erreur}
                return render(request , 'users/create_user.html' , context)
        
            if not re.search(r'[a-z]',password):
                erreur=True
                context={'erreur':erreur}
                return render(request , 'users/create_user.html' , context)


            user= User.objects.create_user(username=username , email=email , password=password)
            profile = Profile.objects.create(user=user , role=role , fullname=fullname)

            return redirect('user_list')
        else :
            erreur=False
            context={'profile':profile , 'erreur':erreur}
            return render(request,'users/create_user.html',context)
    else:
        return render(request , 'permission.html')


def user_list(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        profiles = Profile.objects.all()
        context={'profiles':profiles , 'profile':profile}
        return render(request,'users/user_list.html',context)
    else:
        return render(request , 'permission.html')
    
def user_delete(request,username):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        user = User.objects.get(username=username)
        Profile.objects.filter(user=user).delete()
        return redirect('user_list')
    else:
        return render(request , 'permission.html')
    
def user_edit(request,username):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            fullname = request.POST.get('fullname')
            email = request.POST.get('email')
            role = request.POST.get('role')

            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)

            user.username = username
            user.password = password
            user.email = email

            profile.fullname = fullname
            profile.role = role

            user.save()
            profile.save()

            return redirect('superadmin') 
        else:
            user = User.objects.get(username=username)
            profile = Profile.objects.get(user=user)
            adminapp = (profile.role=='adminapp')
            superviseur = (profile.role=='superviseur')
            context = {'Profile':profile , 'adminapp':adminapp , 'superviseur':superviseur}
            return render(request,'users/create_user.html',context)
    else:
        return render(request , 'permission.html')
    
def platform_list(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        platforms = Platform.objects.all()
        context = {'platforms':platforms , 'profile':profile}
        return render(request,'platforms/list_platforms.html',context)
    else:
        return render(request,'permission.html')
    
def platform_create(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        if request.method=='POST':
            nom = request.POST.get('nom')
            departement = request.POST.get('departement')
            url = request.POST.get('url')

            platform = Platform.objects.create(nom=nom , departement=departement , url=url)

            return redirect('platform_list')
        else:
            context={'profile':profile}
            return render(request,'platforms/create_platform.html',context)
    else: 
        return render(request,'permission.html')
    

def platform_edit(request,platform_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        if request.method=='POST':
            nom = request.POST.get('nom')
            departement = request.POST.get('departement')
            url = request.POST.get('url')

            platform = Platform.objects.get(id=platform_id)
            platform.nom = nom
            platform.departement = departement
            platform.url = url

            platform.save()

            return redirect('platform_list')
        else:
            platform = Platform.objects.get(id=platform_id)
            context = {'platform':platform , 'profile':profile} 

            return render(request,'platforms/create_platform.html',context)
    else:
        return render(request,'permission.html',context)
    
def platform_delete(request,platform_id):
    user = request.user
    profile = Profile.objects.get(user=user)
    if profile.role=='admin':
        platform = Platform.objects.get(id=platform_id)
        platform.delete()
        return redirect('platform_list')
    else:
        return render(request , 'permission.html')
    