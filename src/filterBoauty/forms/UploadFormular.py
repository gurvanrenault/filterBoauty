from django import forms
from django.core.validators import FileExtensionValidator

"""
     Formulaire d'upload d'image 
"""
class UploadFormular(forms.Form):

     file = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg','png'])])
