from dynamic.sun import SunCreator
from dynamic.texture import TextureCreator


__author__ = 'mdorfinger, mkanyildiz'

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class Sonnensystem(object):
    colorsun = None
    zaehler = 0
    sun = SunCreator(2)

    __texture = None

    def __init__(self):
        self.zaehler = 0

        self.sun = SunCreator(2)
        self.__texture = TextureCreator()



    def main(self):
        global event
        pygame.init()
        display = (800,600)

        pygame.display.set_caption("Solarsystem")

        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


        glClearColor(0.,0.,0.,1.)

        gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

        #glTranslatef(-4,0, -50)
        gluLookAt(	0, 0, -50,
                    0, 0,  0,
                    0, 1,  1)
        #glRotatef(0, 2, 1, 0)
        glTranslatef(0,1,0.0)

        zaehlerMoon = 0
        zaehlerPersp = 0
        self.colorsun = glColor3f(1, 1, 0)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


                if event.type == pygame.MOUSEBUTTONDOWN:
                    zaehlerPersp = zaehlerPersp+1

                    #Zoom in
                    if event.button == 4:

                        # Set the camera
                        gluLookAt(0, 0,1,
                                0, 0,  0,
                                0, 1,  0)

                        #glRotatef(90, 2, 1, 0)

                    #Zoom out
                    if event.button == 5:
                            # Set the camera
                        gluLookAt(0, 0,-1,
                                0, 0,  0,
                                0, 1,  0)

                        gluLookAt(0, 0,1,
                            0, 0,  0,
                            0, 1,  0)

                        gluLookAt(0, 0,-1,
                                0, 0,  0,
                                0, 1,  0)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.sun.lightZeroPosition = [0.,0.,0.,0]
                        self.colorsun = glColor3f(0.05, 0.05, 0.05)
                    if event.key == pygame.K_o:
                        self.sun.lightZeroPosition = [0.,0.,0.,1]
                        self.colorsun = glColor3f(1, 1, 0)
                    if event.key == pygame.K_w:
                        gluLookAt(0, 1,0,
                                0, 0,  0,
                                0, 0,  1)


            self.zaehler = self.zaehler+1

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            self.sun.createSun(self.zaehler)

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(""+ str(pygame.MOUSEBUTTONDOWN))
                self.__texture.textureChange()


            pygame.display.flip()
            pygame.time.wait(10)

