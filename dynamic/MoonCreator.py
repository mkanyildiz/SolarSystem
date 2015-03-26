from OpenGL.GL import *

from dynamic.texture import TextureCreator


__author__ = 'Muhammed5, mdorfinger'

class MoonCreator():
    __view = None

    def __init__(self):
        self.__view = TextureCreator()


    def createMoon(self,zaehler,distanz,speed):

        #Moon
        glPushMatrix()
        color = [0.211,0.211,0.211,1.]
        glMaterialfv(GL_FRONT,GL_DIFFUSE,color)

        #Rotation um den Planeten
        glRotatef(speed* zaehler, 0, 1, 0)
        glTranslatef(-distanz, 0, 0)

        #rotation um die eigene achse
        glRotatef(5* zaehler, 0, 1, 0)

        self.__view.txtmond = self.__view.loadTexture("./textures/moon.jpg")
        self.__view.sphere(0.2, self.__view.txtmond)
        glPopMatrix()

