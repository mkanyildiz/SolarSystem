__author__ = 'Muhammed5, mdorfinger'

from OpenGL.GL import *

from dynamic.texture import TextureCreator


class MoonCreator():
    """
    Diese Klasse xyz
    """

    __view = None

    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """
        self.__view = TextureCreator()


    def createMoon(self,zaehler,distanz,speed):
        """
        Diese Methode xyz
        :param zaehler: ist für die Rotation zuständig. Bei jedem durchlauf der while schleife wird diese variable hochgezählt und der Rotationswinkel wird geändert dadurch wird das Rotieren ermöglicht
        :param distanz: distanz zwischen mond und planet
        :param speed:   geschwindigkeit der rotation um den Planeten
        :return:
        """
        #Moon
        glPushMatrix()
        color = [0.211,0.211,0.211,1.]
        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)

        #Rotation um den Planeten
        glRotatef(speed* zaehler, 0, 1, 0) #zuerst wird rotiert
        glTranslatef(-distanz, 0, 0)       # und dann um die gewünschte distanz verschoben

        #rotation um die eigene achse
        glRotatef(5* zaehler, 0, 1, 0)     #rotation um die eigene Achse

        #anzeigen der texturen
        self.__view.txtmond = self.__view.loadTexture("./textures/moon.jpg")
        self.__view.sphere(0.2, self.__view.txtmond)
        glPopMatrix()

