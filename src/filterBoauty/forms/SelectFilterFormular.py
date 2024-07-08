from django import forms
from django.core.validators import FileExtensionValidator
from filterBoauty.models.ImageHandler import ImageHandler
"""
     Formulaire de choix 
"""
FILTER_CHOICES =( 
    ("sepia", "Sepia"), 
    ("indie", "Indie"),
    ("antartica", "Antartica"), 
    ("farwest", "Far west") 
) 
class SelectFilterFormular(forms.Form):

     filter = forms.ChoiceField(label=("Veuillez choisir le filtre de votre choix"),choices=FILTER_CHOICES, widget=forms.Select(attrs={'class':'form-control'}))
