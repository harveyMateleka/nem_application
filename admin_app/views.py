from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import *
from django.core.paginator import Paginator
from django.views import View
from django.urls import path,include,reverse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
# Create your views here.
from .forms import HopitalForm

    


class UtilisateurViews(View):
    def get(self, request, *args, **kwargs):
         result=User_hopital.objects.all().values('name_user','id','username','email','genre','type_user__name_type','admin_users__username','etat','photos').order_by('-id')
         paginator=Paginator(result,3)
         page_number=request.GET.get('page',1)
         try:
            page_obj = paginator.page(page_number)
         except PageNotAnInteger:
            page_obj = paginator.page(1)
         except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)
         context={
            "users":page_obj,
            "categorie":Type_users.objects.all()[:1],
                }
         return render(request, 'liste_utilisateur.html',context)
    
    def post(self, request,):
        if request.method == 'POST' and request.FILES:
            #print(request.FILES.get('img'))
            if request.POST.get('code') and request.POST.get('code') is not None:
                resultat=User_hopital.objects.get(id=self.request.POST.get('code'))
                if resultat:
                    resultat.etat=False
                    resultat.save()
                    return redirect(reverse('admin_app:index_users'))
                
            else:
                if self.request.POST.get('password') != self.request.POST['password']:
                    messages.error(self.request, 'verifiez bien le mot de passe')
                    return redirect(reverse('admin_app:index_users'))  
                try:
                    resultat=User_hopital.objects.get(email=self.request.POST['email'])
                    if resultat:
                        messages.error(self.request, 'cette adresse appartient deja à un utilisateur')
                        return redirect(reverse('admin_app:index_users')) 
                except User_hopital.DoesNotExist:
                        User_hopital.objects.create(
                            name_user=self.request.POST.get('name'),
                            username=self.request.POST.get('username'),
                            email=self.request.POST.get('email'),
                            password=make_password(self.request.POST.get('password')),
                            genre=self.request.POST.get('sexe'),
                            photos=self.request.FILES.get('img'),
                            type_user_id=self.request.POST.get('categorie'),
                            admin_users_id=self.request.user.id,
                            )
                        return redirect(reverse('admin_app:index_users'))
        else:
            messages.error(self.request, 'error')
            return redirect(reverse('admin_app:index_users')) 

def destroy_user(request):
    result=User_hopital.objects.get(pk=request.GET.get('pk'))
    if result:
        result.etat=False
        result.save()
        return JsonResponse({"success": 200},safe=False)

def get_hopitals(request):
    get_hopital= Hopital.objects.all()
    paginator=Paginator(get_hopital,10)
    page_number=request.GET.get('page',1)
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
        
    return page_obj
    
class HopitalView(View):
    forms = HopitalForm
    template_name ='hopital.html'
    
    def get(self, request, *args, **kwargs):
        context={'hopital': get_hopitals(request),
             'forms':self.forms}
        return render(request, self.template_name,context)
    
            
                 
            
            
        
