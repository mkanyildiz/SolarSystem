
import math
from OpenGL.raw.GLUT import glutSolidSphere
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from random import randint
class sonnensystem:

    def __init__(self):
        self.surface = ((0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6))

    def disableLight(self):

        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)


    def showLight(self):
        glShadeModel(GL_SMOOTH)
        glEnable(GL_CULL_FACE)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glDepthFunc(GL_LESS)
        lightZeroPosition = [0.,0.,0.,1.0]
        lightZeroColor = [0.8,1.0,0.8,1.0] #green tinged

        glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
        glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)

    def Sphere(self,radius):

        self.sphere = gluNewQuadric()
        #gluQuadricDrawStyle(self.sphere,GLU_LINE)
        gluSphere(self.sphere,radius,20,20)
        #glutWireSphere(2,100,20)

    def main(self):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glClearColor(0.,0.,0.,1.)

        gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

        glTranslatef(-4,0, -50)

        #glRotatef(0, 2, 1, 0)
        glTranslatef(5,1,0.0)
        zaehler = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()




                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glRotatef(90, 2, 1, 0)
                    if event.button == 5:
                        glRotatef(-0, 2, 1, 0)

            zaehler = zaehler+1


            color = [0.0,0.,1.,1.]

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            glPushMatrix()

            self.disableLight()
            #color = [1.0,1.,0.,1.]
            #glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glColor3f(1, 1, 0)
            self.Sphere(2)

            self.showLight()
            glPopMatrix()

            glPushMatrix()
            color = [0.0,0.,1.,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(1*zaehler, 0, 1, 0)
            glTranslatef(-5, 0, 0)
            self.Sphere(1.5)
            glPopMatrix()

            glPushMatrix()
            color = [0.0,1.,0.,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(3*zaehler, 0, 1, 0)
            glTranslatef(-10, 0, 0)
            self.Sphere(0.5)
            glPopMatrix()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                        self.disableLight()

            pygame.display.flip()
            pygame.time.wait(10)


xy = sonnensystem()
xy.main()