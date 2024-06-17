from classes.converterFactory import ConveterFactory

def img_converting(img_type, *args):
    factory=ConveterFactory()
    converter = factory.create_converter(img_type,*args)
    return converter.converting()

img_converting("PNGtoGIF", "python.png")
img_converting("PNGtoJPG", "python.png")

img_converting("JPGtoGIF", "python.jpg")
img_converting("JPGtoJPG", "python.jpg")

img_converting("GIFtoPNG", "python.gif")
img_converting("GIFtoJPG", "python.gif")