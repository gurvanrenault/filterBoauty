import time
import os
from filterBoauty.settings import MEDIA_ROOT
class FileUploader():

    def __init__(self) -> None:
        self.AUTHORIZED_MIME  = {"png","jpg","jpeg"}
    
    def handle_uploaded_file(self,f):
        ts = time.time()
        name = f.name
        filename = str(int(ts))+"."+name.split('.')[1]
        print("Création du fichier "+filename+" ...")
        with open(str(MEDIA_ROOT)+"/"+filename, 'wb+') as destination:
           for chunk in f.chunks():
                destination.write(chunk)