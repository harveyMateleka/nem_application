from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class Temespanted(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Admin_utili(AbstractUser):
    nom_complet=models.CharField(max_length=255, blank=True)
    genre=models.CharField(max_length=10, blank=True)
    photo=models.ImageField(upload_to='logo_user/', blank=True,null=True)

    def __str__(self):
        return self.nom_complet

class Province(models.Model):
    name_prov=models.CharField(max_length=255,blank=True)
    
    def __str__(self):
        return self.name_prov

class Ville(models.Model):
    name_ville=models.CharField(max_length=255,blank=True, null=True)
    province=models.ForeignKey(Province,models.PROTECT, null=True, blank=True, related_name='province')
    
    def __str__(self):
        return self.name_ville

class Commune(models.Model):
    name_commune=models.CharField(max_length=255,blank=True, null=True)
    ville=models.ForeignKey(Ville, models.PROTECT, null=True, blank=True,related_name="ville")
    
    def __str__(self):
        return self.name_commune

class Type_users(models.Model):
    name_type = models.CharField(max_length=25,blank=True, null=True)

    def __str__(self):
        return self.name_type

class User_hopital(models.Model):
    name_user = models.CharField(max_length=100,blank=True, null=True)
    username=models.CharField(max_length=30,blank=True, null=True)
    email=models.EmailField(max_length=100,null=True,blank=True,unique=True)
    password=models.CharField(max_length=255,null=True,blank=True)
    genre=models.CharField(max_length=1,default="M", blank=True, null=True)
    photos=models.ImageField(upload_to='logo_user_h/', blank=True,null=True)
    type_user=models.ForeignKey(Type_users,models.PROTECT,null=True, blank=True,related_name="Type_users")
    admin_users=models.ForeignKey(Admin_utili,models.PROTECT,null=True, blank=True,related_name="users")
    etat=models.BooleanField(default=True,null=True)
    
    def __str__(self):
        return self.name_user + ' ' + self.email

class Etablissement(models.Model):
    name_etablissement = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return self.name_etablissement

class Hopital(models.Model):
    name_hopital = models.CharField(max_length=255,blank=True, null=True)
    adresse_hopital = models.CharField(max_length=60,blank=True, null=True)
    communes=models.ForeignKey(Commune,models.PROTECT,null=True, blank=True,related_name="commune")
    user=models.ForeignKey(User_hopital,models.PROTECT,null=True, blank=True,related_name="tab_user")
    numero=models.CharField(max_length=15,blank=True,null=True)
    email_hopital=models.CharField(max_length=70,blank=True, null=True)
    def __str__(self):
        return self.name_hopital
    
    
    
