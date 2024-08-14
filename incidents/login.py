from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import Profile

def loginView(request):
    error_login = False
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request , username=username , password=password)

        if user is not None:
            login(request,user)
            profile = Profile.objects.get(user=user)

            if profile.role=='adminapp':
                return redirect('adminapp')
            elif profile.role=='superviseur':
                return redirect('adminapp')
            elif profile.role=='admin':
                return redirect('superadmin')
        else:
            error_login=True
            context = {'error_login':error_login}
            return render(request,'users/login.html',context)
    else:
        context = {'error_login':error_login}
        return render(request,'users/login.html',context)

def logoutView(request):
    logout(request)
    return redirect('login')