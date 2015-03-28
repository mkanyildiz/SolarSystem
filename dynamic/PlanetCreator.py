import string
from docutils.utils.roman import OutOfRangeError

__author__ = 'Muhammed5'

from dynamic.MoonCreator import MoonCreator
from dynamic.texture import TextureCreator
from OpenGL.GL import *


class PlanetCreator():
    """
    Diese Klasse xyz
    """

    __view = None
    __moon = None


    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """
        self.zaehlerMoon = None
        self.__view = TextureCreator()
        self.__moon = MoonCreator()



        #self.__moon = MoonCreator()

    def createPlanet(self,zaehler, abstand, speed, texture, monde, size, moonData):
        """
        Diese Methode xyz
        :param zaehler: ist für die Rotation zuständig. Bei jedem durchlauf der while schleife wird diese variable hochgezählt und der Rotationswinkel wird geändert dadurch wird das Rotieren ermöglicht
        :param abstand: distanz zwischen planet und Sonne
        :param speed: Rotations egschwindigkeit wird übergeben
        :param texture: die art der Textur (Erde, Merkur)
        :param monde: anzahl der Monde
        :return:
        """
        if isinstance(size, (int,float)):
            if size <= 0:
                raise ZeroDivisionError("Size muss größer 0 sein")
            elif isinstance(abstand,(int,float)):
                if isinstance(speed,(int,float)):
                    if isinstance(monde,(int)):
                        if monde < 0:
                            raise OutOfRangeError("monde muss größer 0 sein")
                        elif isinstance(texture, str):
                            #blau
                            glPushMatrix()

                            #rotation um die Sonne
                            glRotatef(speed*zaehler, 0, 1, 0)   #zuerst rotieren
                            glTranslatef(-abstand, 0, 0)        #und dann um die gewünschte distanz verschieben

                            #rotation um die eigene achse
                            glRotatef(24*zaehler, 0, 1, 0)

                            self.__view.txterde = self.__view.loadTexture(texture)
                            glRotate(90, 1, 0, 0)
                            self.__view.sphere(size, self.__view.txterde)
                            glRotate(-90, 1, 0, 0)
                            for x in range(0, monde):
                                self.__moon.createMoon(zaehler,
                                                       moonData[0][x],
                                                       moonData[1][x],
                                                       moonData[2][x])
                            glPopMatrix()
                        else:
                            raise TypeError("ONLY STRING VALUES ARE ALLOWED AS TEXTURE PARAMETER")
                    else:
                        raise TypeError("ONLY INTEGER VALUES ARE ALLOWED")
                else:
                    raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")
            else:
                raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")
        else:
            raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")