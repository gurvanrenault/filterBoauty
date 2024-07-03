from django import forms
from django.core.validators import FileExtensionValidator
class UploadFormular(forms.Form):

     file = forms.ImageField(validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg','png'])])
