from .converter import Converter
import os

class JPGtoGIF (Converter):
    def __init__(self, img_type, img_address):
        super().__init__(img_type)
        self.img_address=img_address

    def converting(self):
        size=len(self.img_address)
        img_name=self.img_address[:size-3]
        os.rename(self.img_address, img_name+"gif")