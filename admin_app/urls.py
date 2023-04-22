from django.contrib import admin
from django.urls import path,include,reverse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, permission_required
app_name='admin_app'
from .views import *

def check(request):
    
    if request.user.username:
         return redirect(reverse('admin_app:home'))
    if request.method=='GET':
        return render(request, 'login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('admin_app:home'))
    else:
        return redirect(reverse('check'))

def uncheck(request):
    logout(request)
    return redirect(reverse('check'))

def home(request):
    return render(request,'home.html')


urlpatterns = [
    path('',check,name="checks"),
    path('home',home,name="home"),
    path('liste_users',UtilisateurViews.as_view(),name="index_users"), 
    path('delete_admin_hopi',destroy_user,name="destroy_user"), 
    path('hopital',HopitalView.as_view(),name="hopital"), 
]