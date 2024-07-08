from PIL import Image,ImageEnhance
import numpy as np
import random 

# This class handle the filters applied to images 

class Filters: 

    """
        Filter sépia
        @param img : image to modify 
        @return image modified 
    """

    def sepia(img: Image)->Image:
        
        width, height = img.size
        pixels = img.load()
        for py in range(height):
            for px in range(width):
                r, g, b = img.getpixel((px, py))

                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)

                if tr > 255:
                    tr = 255

                if tg > 255:
                    tg = 255

                if tb > 255:
                    tb = 255

                pixels[px, py] = (tr,tg,tb)

        return img

    """
        Filter INDIE
        @param img : image to modify 
        @return image modified 
    """
    def indie(img: Image)->Image:
        img= Filters.addNoise(img,0.02)
        img= Filters.enhanceSaturation(img,2.47)
        return img 
    
    """
        Filter ANTARTICA
        @param img : image to modify 
        @return image modified 
    """
    def antartica(img:Image)->Image:
        matrix = (0.07891889953964326, 0.6121557603819253, 0.9581835902639521,0.4391222562107975,
                   0.46740023535170283, 0.8767655406999929,0.8782759007897254, 0.8823922697054689, 
                   0.9033046752732915, 0.9805843409686572, 0.09100247841564835, 0.3778710942453125)
        img = img.convert("RGB", matrix)
        return img
    
    """
        Filter FAR WEST
        @param img : image to modify 
        @return image modified 
    """
    def farwest(img:Image)->Image:
        matrix = (0.7868854105884159, 0.14494583677528716, 0.44905046302954854, 0.2596145929943917,
                  0.32501857212215146, 0.7965111006084229, 0.6275831795667688, 0.6341024781143401,
                  0.3478819863064878, 0.25459073828476997, 0.9248951628790252, 0.049728751307545394)
        img= Filters.enhanceSaturation(img,2.47)
        img= Filters.addNoise(img,0.05)
        img = img.convert("RGB", matrix)
        return img
    
    """
        Filter with a random matrix generated , used to generate new filters
        Use this to create new filters
        @param img : image to modify 
        @return image modified 
    """
    
    def random(img:Image)->Image:
        matrix = ( random.random(), random.random(), random.random(), random.random(),
                    random.random(), random.random(), random.random(), random.random(),
                    random.random(), random.random(), random.random(), random.random())
        print(matrix)
        img = img.convert("RGB", matrix)
        return img

    """
        Saturate an image
        @param img : image to modify 
        @param factor : factor of enhancement
        @return image modified 
    """
    def enhanceSaturation(image, factor=1)->Image:

        converter = ImageEnhance.Color(image)
        return converter.enhance(factor)

    """
        Noisify an image
        @param img : image to modify 
        @param factor : factor of enhancement
        @return image modified 
    """
    def addNoise(image, amount=0.02):
        np_image = np.array(image)
        noise = np.random.normal(0, amount * 255, np_image.shape)
        np_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(np_image)
    
    """
        Noisify an image
        @param img : image to modify 
        @param filtername : name of the filter
        @return image modified 
    """
    def applyFilter(self,filtername,img):
        filter = getattr(Filters,filtername)
        return filter(img)