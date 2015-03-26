from dynamic.MoonCreator import MoonCreator
from dynamic.texture import TextureCreator

__author__ = 'Muhammed5'

from OpenGL.GL import *


class PlanetCreator():
    """
    Diese Klasse xyz
    """

    __view = None
    __moon = None
    zaehlerMoon = None
    zaehler = 0
    __distanzMond = []
    __speedMoon = []

    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """
        self.zaehlerMoon = None
        self.__view = TextureCreator()
        self.__moon = MoonCreator()
        self.zaehlerMoon =0
        self.__distanzMond = [2,3]
        self.__speedMoon = [2,5]


        #self.__moon = MoonCreator()

    def createPlanet(self,zaehler, abstand, speed, texture, monde):
        """
        Diese Methode xyz
        :param zaehler:
        :param abstand:
        :param speed:
        :param texture:
        :param monde:
        :return:
        """
        #blau
        glPushMatrix()

        #rotation um die Sonne
        glRotatef(speed*zaehler, 0, 1, 0)
        glTranslatef(-abstand, 0, 0)

        #rotation um die eigene achse
        glRotatef(5*zaehler, 0, 1, 0)

        self.__view.txterde = self.__view.loadTexture(texture)
        self.__view.sphere(1.5, self.__view.txterde)
        self.zaehlerMoon += 1
        for x in range(0, monde):
            self.__moon.createMoon(self.zaehlerMoon,self.__distanzMond[x],self.__speedMoon[x])

        glPopMatrix()