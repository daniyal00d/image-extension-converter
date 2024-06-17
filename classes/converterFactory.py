from .JPGtoPNG import JPGtoPNG
from .PNGtoJPG import PNGtoJPG
from .JPGtoGIF import JPGtoGIF
from .PNGtoGIF import PNGtoGIF
from .GIFtoJPG import GIFtoJPG
from .GIFtoPNG import GIFtoPNG

class ConveterFactory:
    def create_converter(self, img_type, *args):
        self.converter_classes = {
            "JPGtoPNG": JPGtoPNG,
            "PNGtoJPG": PNGtoJPG,
            "JPGtoGIF":JPGtoGIF,
            "PNGtoGIF":PNGtoGIF,
            "GIFtoPNG":GIFtoJPG,
            "GIFtoPNG":GIFtoPNG
        }
        converter_class = self.converter_classes.get(img_type)
        return converter_class(img_type,*args)