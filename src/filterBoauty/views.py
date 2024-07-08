from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from filterBoauty.models.Filters import Filters

from .forms.SelectFilterFormular import SelectFilterFormular
from .forms.UploadFormular import UploadFormular
from .models.ImageHandler import ImageHandler

"""
    Route to upload an image 

"""
def index (request):
    if request.method == 'POST':
        form = UploadFormular(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            uploader = ImageHandler()
            filename = uploader.uploadFile(request.FILES['file'])
            return HttpResponseRedirect('/filters/'+filename)
        print(form.errors) 
    form = UploadFormular()
    context  = { "form" : form}
    return render(request, "index.html", context)

def filters(request,filename):
    
    form = SelectFilterFormular()
    context= {
              "filename": filename, 
              "filters" : ImageHandler.getNativeFiltersBase64(filename),
              "form":form
            } 
    return render(request, "filters.html", context)

def download(request):
    if request.method == 'POST':
            print("ARARR")
            form = SelectFilterFormular(request.POST)
            if form.is_valid():
                filename = request.POST['filename']
                filtername = request.POST['filter'].lower()
                filterHandler = Filters()
                imagehandler = ImageHandler()
                img = ImageHandler.getUploadedImage(filename)
                imgFiltered= filterHandler.applyfilter(filtername,img)
                imagehandler.uploadImage(imgFiltered,filename)
                return imagehandler.download(filename)

    return HttpResponseRedirect('/')