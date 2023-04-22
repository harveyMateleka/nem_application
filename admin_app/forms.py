from .models import *
from django import forms

class HopitalForm(forms.ModelForm):
    class Meta:
        model = Hopital
        fields ="__all__"
        widget={
            "name_hopital":forms.TextInput(attrs={'placeholder':"veuillez entrer le nom de l'hopital","class":"form-control","required":True}),
            "adresse_hopital":forms.TextInput(attrs={'placeholder':"veuillez entrer l'adresse de l'hopital","class":"form-control","required":True}),
            "communes":forms.Select(attrs={'placeholder':"veuillez choisir la comune","class":"form-control select","required":True}),
            "user":forms.Select(attrs={'placeholder':"veuillez choisir l'administrateur","class":"form-control select","required":True}),
            "email_hopital":forms.TextInput(attrs={'placeholder':"veuillez entrer l'adresse email","class":"form-control","required":True}),
            "numero":forms.TextInput(attrs={'placeholder':"veuillez entrer le numéro","class":"form-control","required":True}),
            
        }
        