__author__ = 'mdorfinger, mkanyildiz'

from dynamic.SunCreator import SunCreator
from dynamic.texture import TextureCreator

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


class Sonnensystem(object):
    """
    Diese Klasse erstellt ein pygame-Fenster, erstellt die Planeten und die Tastensteuerung wird hier ausprogrammiert.
    """
    colorsun = None
    zaehler = 0
    sun = SunCreator(2)

    __texture = None

    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :param anzPlanet: Die anzahl der Planeten die gezeichnet werden müssen
        :return:
        """
        self.zaehler = 0

        self.sun = SunCreator(2)
        self.__texture = TextureCreator()



    def main(self):
        """
        Diese Methode ist für die Visualisierung der Elemente zuständlich hier enden alle Objekte
        :return:
        """
        global event
        #wir definieren das fenster
        pygame.init()
        display = (800,600)

        # hier wird der titel des Fensters definiert
        pygame.display.set_caption("Solarsystem")

        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        #Die anfangs farben werden definiert
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
        #diese whileschleife ist sehr wichtig für das refreshen der objekte
        while True:
            #mit dieser forschleife können wir auf benutzer eingaben zugreifen und mit if unterscheidungen auf
            # diese reagieren
            for event in pygame.event.get():
                #beim fenster-schließen wird das ganze programm beendet
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                #Hier reagieren wir auf ein Mousbutton event
                if event.type == pygame.MOUSEBUTTONDOWN:
                    zaehlerPersp = zaehlerPersp+1

                    #Zoom in
                    if event.button == 4:

                        # Set the camera
                        gluLookAt(0, 0, 1,
                                0, 0,  0,
                                0, 1,  0)

                        #glRotatef(90, 2, 1, 0)

                    #Zoom out
                    if event.button == 5:
                            # Set the camera
                        gluLookAt(0, 0, -1,
                                0, 0,  0,
                                0, 1,  0)

                        gluLookAt(0, 0, 1,
                            0, 0,  0,
                            0, 1,  0)

                        gluLookAt(0, 0, -1,
                                0, 0,  0,
                                0, 1,  0)

                #Hier reagieren wir auf ein KEY event
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
                    if event.key == pygame.K_t:
                        self.__texture.textureChange()

            # Die Variable Zaehler iwrd bei jedem durchgang hoch gezählt, diese Variable wird später
            # an die Klasse SOnne und von dort an die Klasse Planet weiter gegeben da der Planet sein Rotations Winkel
            # ändern muss um sich drehen zu können
            self.zaehler = self.zaehler+1

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
            #die methode createSun wird aufgerufen
            self.sun.createSun(self.zaehler)

            pygame.display.flip()
            pygame.time.wait(10)