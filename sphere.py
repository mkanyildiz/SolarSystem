
import math
from OpenGL.raw.GLUT import glutSolidSphere
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import *

from random import randint
class sonnensystem:

    lightZeroPosition = []
    colorsun = None

    def __init__(self):
        self.lightZeroPosition = [0.,0.,0.,1]
        self.surface = ((0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6))
        self.txtmerkur = None
        self.txterde = None
        self.txtsonne = None
        self.txtmond = None
        self.mod = True

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

    def LoadTexture(self, pic):
        if pic == "erde":
            # Bild auswaehlen
            image = open("./textures/erde.jpg")
        elif pic == "sonne":
            image = open("./textures/sonne.jpg")
        elif pic =="merkur":
            image = open("./textures/merkur.jpg")
        elif pic == "mond":
            image = open("./textures/moon.jpg")

        # Textur
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        #glEnable(GL_TEXTURE_2D)
        textures = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, textures)  # 2d texture (x and y size)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return textures

    def Sphere(self,radius, txt):

        quadratic = gluNewQuadric()

        gluQuadricNormals(quadratic, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(quadratic, GL_TRUE)  # Create Texture Coords (NEW)
        #gluQuadricDrawStyle(self.sphere,GLU_LINE)

        glBindTexture(GL_TEXTURE_2D, txt)
        gluSphere(quadratic,radius,20,20)
        #glutWireSphere(2,100,20)

    def textureChange(self):
        if self.mod is True:
            glEnable(GL_TEXTURE_2D)
            self.mod = False
            self.txtmerkur = self.LoadTexture("merkur")
            self.txtsonne = self.LoadTexture("sonne")
            self.txterde = self.LoadTexture("erde")
            self.txtmond  = self.LoadTexture("mond")
        else:
            glDisable(GL_TEXTURE_2D)
            self.mod = True

    def main(self):
        pygame.init()
        display = (800,600)

        pygame.display.set_caption("Solarsystem")

        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glClearColor(0.,0.,0.,1.)

        gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

        glTranslatef(-4,0, -50)

        #glRotatef(0, 2, 1, 0)
        glTranslatef(5,1,0.0)
        zaehler = 0
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
                    if event.button == 4:
                        glLoadIdentity()
                        # Set the camera
                        gluLookAt(	0, 0, 0,
                        0, 0,  50,
                        0, 0,  0)

                        #glRotatef(90, 2, 1, 0)
                    if event.button == 5:
                        glTranslatef(-4,0, 1*-(zaehlerPersp))
                        #glRotatef(-0, 2, 1, 0)

            zaehler = zaehler+1


            #color = self.sunlight

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


            #Sonne
            glPushMatrix()
            self.disableLight()
            self.colorsun
            self.txtsonne = self.LoadTexture("sonne")
            self.Sphere(2, self.txtsonne)
            self.showLight()
            glPopMatrix()

            #blau
            glPushMatrix()
            #color = [0.0,0.,1.,1.]
            #glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(1*zaehler, 0, 1, 0)
            glTranslatef(-5, 0, 0)
            self.txterde = self.LoadTexture("erde")
            self.Sphere(1.5, self.txterde)
            zaehlerMoon = zaehlerMoon+1

            #Moon
            glPushMatrix()
            color = [0.211,0.211,0.211,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(5*zaehlerMoon, 0, 1, 0)
            glTranslatef(-2, 0, 0)
            self.txtmond = self.LoadTexture("mond")
            self.Sphere(0.5, self.txtmond)
            glPopMatrix()

            glPopMatrix()

            #grün
            glPushMatrix()
            #color = [0.0,1.,0.,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(3*zaehler, 0, 1, 0)
            glTranslatef(-10, 0, 0)
            self.txtmerkur = self.LoadTexture("merkur")
            self.Sphere(0.5, self.txtmerkur)
            glPopMatrix()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.lightZeroPosition = [0.,0.,0.,0]
                        self.colorsun = glColor3f(0.05, 0.05, 0.05)
                    if event.key == pygame.K_o:
                        self.lightZeroPosition = [0.,0.,0.,1]
                        self.colorsun = glColor3f(1, 1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(""+ str(pygame.MOUSEBUTTONDOWN))
                self.textureChange()


            pygame.display.flip()
            pygame.time.wait(10)


xy = sonnensystem()
xy.main()
