from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms.UploadFormular import UploadFormular
from .models.FileUploader import FileUploader


def index (request):
    if request.method == 'POST':
        form = UploadFormular(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            uploader = FileUploader()
            uploader.handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
        print(form.errors) 
    form = UploadFormular()
    context  = { "form" : form}
    return render(request, "index.html", context)
