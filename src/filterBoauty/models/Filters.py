from PIL import Image,ImageEnhance
import numpy as np
class Filters: 
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

    def indie(img: Image)->Image:
        img= Filters.add_noise(img,0.10)
        img= Filters.enhance_saturation(img,2.47)
        return img 
    
    def enhance_saturation(image, factor=1):
        converter = ImageEnhance.Color(image)
        return converter.enhance(factor)
    
    def add_noise(image, amount=0.02):
        np_image = np.array(image)
        noise = np.random.normal(0, amount * 255, np_image.shape)
        np_image = np.clip(np_image + noise, 0, 255).astype(np.uint8)
        return Image.fromarray(np_image)
    
    def applyfilter(self,filtername,img):
        filter = getattr(Filters,filtername)
        return filter(img)