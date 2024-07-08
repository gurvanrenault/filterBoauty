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
            filename = uploader.upload_file(request.FILES['file'])
            return HttpResponseRedirect('/filters/'+filename)
        print(form.errors) 
    form = UploadFormular()
    context  = { "form" : form}
    return render(request, "index.html", context)

"""
    Route to select filters
"""
"""
    Route to select filters
"""
def filters(request,filename):
    
    form = SelectFilterFormular()
    context= {
              "filename": filename, 
              "filters" : ImageHandler.get_filters_images(filename),
              "form":form
            } 
    return render(request, "filters.html", context)

"""
    Route to download an image
"""
def download(request):
    if request.method == 'POST':
            form = SelectFilterFormular(request.POST)
            if form.is_valid():
                filename = request.POST['filename']
                filtername = request.POST['filter'].lower()
                filterHandler = Filters()
                imagehandler = ImageHandler()
                img = ImageHandler.get_uploaded_image(filename)
                imgFiltered= filterHandler.apply_filter(filtername,img)
                imagehandler.upload_image(imgFiltered,filename)
                return imagehandler.download(filename)

    return HttpResponseRedirect('/')