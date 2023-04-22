from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Etablissement)
class AdminEtablissement(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ("id","name_etablissement",)
    search_fields = ['name_etablissement',]


@admin.register(Type_users)

class AdminType_users(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ("id","name_type",)
    search_fields = ['name_type',]

@admin.register(Commune)

class AdminCommune(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ("id","name_commune",)
    search_fields = ['name_commune',]

@admin.register(Ville)

class AdminVille(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ("id","name_ville",)
    search_fields = ['name_ville',]

@admin.register(Province)

class AdminProvince(admin.ModelAdmin):
    ordering = ('-id',)
    list_display = ("id","name_prov",)
    search_fields = ['name_prov',]