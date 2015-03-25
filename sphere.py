__author__ = 'mdorfinger, mkanyildiz'



import math
from OpenGL.raw.GLUT import glutSolidSphere
import pygame

from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import *

from random import randint
class Sonnensystem:

    lightZeroPosition = []
    colorsun = None

    def __init__(self):
        """

        :return:
        """
        self.lightZeroPosition = [0.,0.,0.,1]
        self.surface = ((0,1,2,3),
        (3,2,7,6),
        (6,7,5,4),
        (4,5,1,0),
        (1,5,7,2),
        (4,0,3,6))

        # Die Variablen für die Texturen werden deklariert
        self.txtmerkur = None
        self.txterde = None
        self.txtsonne = None
        self.txtmond = None
        # mod braucht man um die Textur zu wechseln.
        self.mod = True

    def disableLight(self):
        """

        :return:
        """
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)


    def showLight(self):
        """

        :return:
        """
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

    def loadTexture(self, bild):
        """
        Diese Methode lädt die Bilder die auf die Planeten gegeben werden.

        :param bild: Es wird angegeben welches Bild geöffnet werden soll.
        :return: Die Textur ID
        """

        image = open(bild) # Das Bild wird geladen.

        # Textur
        ix = image.size[0] # Größe der Textur (Horizontal)
        iy = image.size[1] # Größe der Textur (Vertikal)
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        textures = glGenTextures(1) # Textur ID
        glBindTexture(GL_TEXTURE_2D, textures)  # 2d texture (x and y size)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

        return textures #ID wird zurückgegeben

    def sphere(self, radius, txt):
        """
        Diese Methode erstellt ein Sphere und legt die Textur darauf.
        :param radius: Wiegroß die Sphere sein soll.
        :param txt: Welche Textur raufgelegt werden soll.
        :return:
        """

        quadratic = gluNewQuadric()

        gluQuadricNormals(quadratic, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(quadratic, GL_TRUE)  # Create Texture Coords (NEW)
        #gluQuadricDrawStyle(self.sphere,GLU_LINE)

        glBindTexture(GL_TEXTURE_2D, txt) # Textur auf Objekt legen
        gluSphere(quadratic,radius,30,30) # Sphere wird erstellt
        #glutWireSphere(2,100,20)

    def textureChange(self):
        """
        Diese Methode sorgt dafür, dass die Textur ein bzw ausgeschalten wird.
        :return:
        """
        if self.mod is True:
            self.mod = False
            glEnable(GL_TEXTURE_2D)
            self.txtmerkur = self.loadTexture("./textures/merkur.jpg")
            self.txtsonne = self.loadTexture("./textures/sonne.jpg")
            self.txterde = self.loadTexture("./textures/erde.jpg")
            self.txtmond  = self.loadTexture("./textures/moon.jpg")
        else:
            self.mod = True
            glDisable(GL_TEXTURE_2D)

    def main(self):
        """
        :return:
        """
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


            zaehler = zaehler+1


            #color = self.sunlight

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


            #Sonne
            glPushMatrix()
            self.disableLight()
            self.colorsun
            self.txtsonne = self.loadTexture("./textures/sonne.jpg") # Textur wird geladen
            self.sphere(2, self.txtsonne) # Sphere wird erstellt
            self.showLight()
            glPopMatrix()

            #blau
            glPushMatrix()

            #rotation um die Sonne
            glRotatef(1*zaehler, 0, 1, 0)
            glTranslatef(-5, 0, 0)

            #rotation um die eigene achse
            glRotatef(5*zaehler, 0, 1, 0)
            self.txterde = self.loadTexture("./textures/erde.jpg") # Textur wird geladen
            self.sphere(1.5, self.txterde) # Sphere wird erstellt
            zaehlerMoon = zaehlerMoon+1

            #Moon
            glPushMatrix()
            color = [0.211,0.211,0.211,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)

            #Rotation um den Planeten
            glRotatef(5*zaehlerMoon, 0, 1, 0)
            glTranslatef(-2, 0, 0)

            #rotation um die eigene achse
            glRotatef(5*zaehlerMoon, 0, 1, 0)

            self.txtmond = self.loadTexture("./textures/moon.jpg") # Textur wird geladen
            self.sphere(0.5, self.txtmond) # Sphere wird erstellt
            glPopMatrix()

            glPopMatrix()

            #grün
            glPushMatrix()

            #rotation um die sonne
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glRotatef(3*zaehler, 0, 1, 0)

            #rotation um die eigene achse
            glRotatef(3*zaehler, 0, 1, 0)
            glTranslatef(-10, 0, 0)
            self.txtmerkur = self.loadTexture("./textures/merkur.jpg") # Textur wird geladen
            self.sphere(0.5, self.txtmerkur) # Sphere wird erstellt
            glPopMatrix()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.lightZeroPosition = [0.,0.,0.,0]
                        self.colorsun = glColor3f(0.05, 0.05, 0.05)
                    if event.key == pygame.K_o:
                        self.lightZeroPosition = [0.,0.,0.,1]
                        self.colorsun = glColor3f(1, 1, 0)

            if event.type == pygame.MOUSEBUTTONDOWN: # wenn die Maus gedrückt wird
                # print(""+ str(pygame.MOUSEBUTTONDOWN))
                self.textureChange() # wird die Textur ein bzw ausgeschalten


            pygame.display.flip()
            pygame.time.wait(10)


# xy = Sonnensystem()
# xy.main()
