from PIL import Image

try:
    im = Image.open("splash.jpg") #image laden
    print(im.format,im.size,im.mode) #infos ueber das bild
    im.show() #image zeigen
except:
    print ("Unable to load image")

#im.show()

#hier wird ein bestimmter Bereich ausgeschnitten
#box = (100, 100, 400, 400) #bereich angeben
#region = im.crop(box) #ausschneiden
#region.show()

#hier wird der ausgschnittene Bereich um 180 grad gedreht wieder eingefügt
#region = region.transpose(Image.ROTATE_180) #rotation
#im.paste(region, box) #einfuegen

#im.show()
