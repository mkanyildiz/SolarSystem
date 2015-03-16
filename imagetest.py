__author__ = 'mdorfinger'

from PIL import Image

try:
    im = Image.open("splash.jpg") #image laden
    print(im.format,im.size,im.mode) #infos ueber das bild
    im.show() #image zeigen
except:
    print ("Unable to load image")
