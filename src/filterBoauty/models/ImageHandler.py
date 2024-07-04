import time
import os
import io
import base64

from django.http import HttpResponse
from filterBoauty.settings import MEDIA_ROOT
from PIL import Image 
from filterBoauty.models.Filters import Filters 

class ImageHandler():
    
    
    AUTHORIZED_MIME  = ["png","jpg","jpeg"]
    FILTERS = ["sepia","indie"]
        
    
    """
        Upload a file 
        param : 
            f : InMemoryUploadedFile  the image file 
     """
    def uploadFile(self,f)-> None: 
        print(type(f).__name__)
        ts = time.time()
        name = f.name
        filename = str(int(ts))+"."+name.split('.')[1]
        print("Création du fichier "+filename+" ...")
        with open(str(MEDIA_ROOT)+"/"+filename, 'wb+') as destination:
           for chunk in f.chunks():
                destination.write(chunk)
        return filename
    
    def uploadImage(self,img:Image,filename)-> None: 
        img.save(os.path.join(str(MEDIA_ROOT),filename))

    def download(self,filename:str)-> HttpResponse:
        file = open(str(MEDIA_ROOT)+"/"+filename, "rb").read()
        response = HttpResponse(file, content_type='image/'+filename.split('.')[1])
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename.split('.')[0]+'-edited.'+filename.split('.')[1])
        return response
    
    def imageToBase64(img :Image):
        output = io.BytesIO()
        img.save(output, format="png")
        return  base64.b64encode(output.getvalue())
    
    
    
    def base64ToImage(b64: str)->Image:
        return Image.open(b64)
    
    def getUploadedImage(filename)->Image:
        return Image.open(os.path.join(MEDIA_ROOT,filename))
   
    def getNativeFiltersBase64(filename:str):
        filters= []
        filterHandler = Filters()
        id = 0 

        img = ImageHandler.getUploadedImage(filename)
        base64 = "data:image/"+filename.split('.')[1]+";base64,"+str(ImageHandler.imageToBase64(img), encoding='utf-8')
        filters.append({  "id":id,"name" : "Original","base64": base64})
        
        for filtername in ImageHandler.FILTERS:
            id+=1
            img = ImageHandler.getUploadedImage(filename)
            imgFiltered= filterHandler.applyfilter(filtername,img)
            base64 = "data:image/"+filename.split('.')[1]+";base64,"+str(ImageHandler.imageToBase64(imgFiltered), encoding='utf-8')
            filters.append({ "id":id,"name" : filtername.title(),"base64": base64}) 
        return filters