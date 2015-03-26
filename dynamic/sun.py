from dynamic.PlanetCreator import PlanetCreator

from dynamic.texture import TextureCreator

__author__ = 'Muhammed5, mdorfinger'

from OpenGL.GL import *


class SunCreator(object):
    __view = None
    __planet = None
    __light = None
    lightZeroPosition = []
    __anzPlanet = 0
    __abstand = []
    __speed = []
    __texture = []
    __anzMonde = []
    def __init__(self,anzPlanet):
        self.__anzPlanet = anzPlanet
        self.__abstand = [5,10]
        self.__speed = [2,5]
        self.__texture = ["./textures/erde.jpg","./textures/merkur.jpg"]
        self.__anzMonde = [1,2]

        self.__view = TextureCreator()
        self.__planet = PlanetCreator()
        self.lightZeroPosition = [0.,0.,0.,1]



    def disableLight(self):

        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)


    def showLight(self):
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glDepthFunc(GL_LESS)


        lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged
        glLightfv(GL_LIGHT0, GL_POSITION, self.lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def createSun(self,zaehler):

            #Sonne
            glPushMatrix()
            self.disableLight()

            self.__view.txtsonne = self.__view.loadTexture("./textures/sonne.jpg")
            self.__view.sphere(2, self.__view.txtsonne)
            self.showLight()
            glPopMatrix()
            for x in range(0, self.__anzPlanet):
                self.__planet.createPlanet(
                    zaehler,self.__abstand[x],
                    self.__speed[x],
                    self.__texture[x],
                    self.__anzMonde[x])