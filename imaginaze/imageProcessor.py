from PIL import ImageFilter, ImageOps

class ImageProcessor:
    def __init__(self, img):
        self.img = img  

    def sharpen(self):
        self.img = self.img.filter(ImageFilter.SHARPEN)  # фильтр резкости
        return self.img  

    def border(self):
        self.img = ImageOps.expand(self.img, border=15, fill='black')  # рамка 15 ph
        return self.img 

