from django.test import Client, TestCase
from filterBoauty.settings import MEDIA_ROOT
import io
import os.path
from PIL import Image

"""
    Tester l'upload d'image  
"""
class ImageUploadTest(TestCase):
    
    """
        Générer une image 
    """
    def generatePhotoFile(self):
            file = io.BytesIO()
            image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
            image.save(file, 'png')
            file.name = 'test.png'
            file.seek(0)
            return file 
    
    """
        Tester l'upload d'image 
    """
    def testUploadFile(self):
        c = Client()
        fp = self.generatePhotoFile()
        c.post('/', {'file': fp})
        