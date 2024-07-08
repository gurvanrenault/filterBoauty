from django import forms
from django.core.validators import FileExtensionValidator
from filterBoauty.models.ImageHandler import ImageHandler


"""
     Formulaire d'upload d'image 
"""

class UploadFormular(forms.Form):

     file = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=ImageHandler.AUTHORIZED_MIME)])
