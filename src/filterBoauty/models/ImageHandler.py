import time
import os
from filterBoauty.settings import MEDIA_ROOT

class ImageHandler():

    def __init__(self) -> None:
        self.AUTHORIZED_MIME  = {"png","jpg","jpeg"}
    
    """
        Upload a file 
        param : 
            f : InMemoryUploadedFile  the image file 
     """
    def uploadFile(self,f):
        
        print(type(f).__name__)
        ts = time.time()
        name = f.name
        filename = str(int(ts))+"."+name.split('.')[1]
        print("Création du fichier "+filename+" ...")
        with open(str(MEDIA_ROOT)+"/"+filename, 'wb+') as destination:
           for chunk in f.chunks():
                destination.write(chunk)