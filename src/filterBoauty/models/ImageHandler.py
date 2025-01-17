import time
import os
import io
import base64

from django.http import HttpResponse
from filterBoauty.settings import MEDIA_ROOT
from PIL import Image 
from filterBoauty.models.Filters import Filters 

# This class handle the upload/download , the application of filters, convert to base64 
class ImageHandler():
    
    
    AUTHORIZED_MIME  = ["png","jpg","jpeg"]
    FILTERS = ["sepia","indie","farwest","antartica"]
        
    
    """
        Upload a file 
        param : 
            f : InMemoryUploadedFile  the image file 
     """
    def upload_file(self,f)-> None: 
        print(type(f).__name__)
        ts = time.time()
        name = f.name
        filename = str(int(ts))+"."+name.split('.')[1]
        with open(str(MEDIA_ROOT)+"/"+filename, 'wb+') as destination:
           for chunk in f.chunks():
                destination.write(chunk)
        return filename
    
     
    """
        Upload an image 
        @param filename : name of the file 
        @param img : image to upload 
     """
    def upload_image(self,img:Image,filename:str)-> None: 
        img.save(os.path.join(str(MEDIA_ROOT),filename))


    """
        Download a file client-side
        @param filename : name of the file 
        @return HttpResponse the reponse to the query containing the file to download  
    """
    def download(self,filename:str)-> HttpResponse:
        file = open(str(MEDIA_ROOT)+"/"+filename, "rb").read()
        response = HttpResponse(file, content_type='image/'+filename.split('.')[1])
        response['Content-Disposition'] = 'attachment; filename={}'.format(filename.split('.')[0]+'-edited.'+filename.split('.')[1])
        return response
    

    """
        Convert an image to base 64
        @param img image to convert
    """
    def image_to_base64(img :Image) -> str:
        output = io.BytesIO()
        img.save(output, format="png")
        return  base64.b64encode(output.getvalue())
    

    """
        Get uploaded image 
        @param filename : name of the file 
        @param img image to open

    """
    def get_uploaded_image(filename)->Image:
        return Image.open(os.path.join(MEDIA_ROOT,filename))
   
    """
        Get uploaded image 
        @param filename : name of the file 
        @return list of base64 encoded images corresponding to filters
    """
    def get_filters_images(filename:str):
        filters= []
        filterHandler = Filters()
        id = 0 

        img = ImageHandler.get_uploaded_image(filename)
        base64 = "data:image/"+filename.split('.')[1]+";base64,"+str(ImageHandler.image_to_base64(img), encoding='utf-8')
        filters.append({  "id":id,"name" : "Original","base64": base64})
        
        for filtername in ImageHandler.FILTERS:
            id+=1
            img = ImageHandler.get_uploaded_image(filename)
            imgFiltered= filterHandler.apply_filter(filtername,img)
            base64 = "data:image/"+filename.split('.')[1]+";base64,"+str(ImageHandler.image_to_base64(imgFiltered), encoding='utf-8')
            filters.append({ "id":id,"name" : filtername.title(),"base64": base64}) 
        return filters