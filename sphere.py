
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
    verticies = (
        (1,     -1, -1),
        (1,     1,  -1),
        (-1,    1,  -1),
        (-1,    -1, -1),
        (1,     -1, 1),
        (1,     1,  1),
        (-1,    -1, 1),
        (-1,    1,  1)
    )

    edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
    )

    surfaces = (

    )

    colors = (
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (0,1,0),
        (1,1,1),
        (0,1,1),
        (1,0,0),
        (0,1,0),
        (0,0,1),
        (1,0,0),
        (1,1,1),
        (0,1,1)
    )

    """def Cube(self):
        glBegin(GL_QUADS)
        x = 0
        for surface in surfaces:
            x = 0
            for vertex in surface:
                x+=1
                glColor3fv(colors[x])
                glVertex3fv(verticies[vertex])

        glEnd()

        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()"""
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
		

    def LoadTexture(self, pic):

        if pic == "erde":
            # Bild auswaehlen
            image = open("./erde.jpg")
        elif pic == "sonne":
            image = open("./sonne.jpg")
        elif pic =="merkur":
            image = open("./merkur.jpg")

        # Textur
        ix = image.size[0]
        iy = image.size[1]
        image = image.tostring("raw", "RGBX", 0, -1)

        # Textur erstellen
        textures = glGenTextures(3)
        glBindTexture(GL_TEXTURE_2D, int(textures[0]))  # 2d texture (x and y size)

        
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
        gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)
		
		return textures

    def Sphere(self,radius,txt):
		glBindTexture(GL_TEXTURE_2D, txt)
        self.sphere = gluNewQuadric()
        #gluQuadricDrawStyle(self.sphere,GLU_LINE)
		
        gluQuadricNormals(self.sphere, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(self.sphere, GL_TRUE)  # Create Texture Coords (NEW)
		gluSphere(self.sphere,radius,32,32)
		
        gluSphere(self.sphere,radius,20,20)
        #glutWireSphere(2,100,20)

    def main(self):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

        glClearColor(0.,0.,0.,1.)

        gluPerspective(45, (display[0]/display[1]), 0.1, 200.0)

        glTranslatef(0,0, -50)

        #glRotatef(0, 2, 1, 0)
        glTranslatef(5,1,0.0)

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





            color = [0.0,0.,1.,1.]

            glTranslatef(-10.0,0,0)
            glRotatef(0.5, 0, 1, 0)
            glTranslatef(10.0,0,0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

            #Blauer Planet
            glPushMatrix()
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            self.Sphere(1)
            glPopMatrix()
			
			

            #Grüner Planet
            glPushMatrix()
            color = [0.0,1.,0.,1.]
            glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glTranslatef(-5, 0, 0)

            glRotatef(0.5, 0, 1, 0)
			self.txtsonne = Texturen.LoadTexture("merkur")
            self.Sphere(1.5)
            glPopMatrix()

            #die sonne
            glPushMatrix()
            glTranslatef(-10, 0, 0)
            self.disableLight()
            #color = [1.0,1.,0.,1.]
            #glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
            glColor3f(1, 1, 0)
			self.txtsonne = Texturen.LoadTexture("sonne")
            self.Sphere(2,self.txtsonne)

            self.showLight()
            glPopMatrix()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
                        #self.disableLight()

            pygame.display.flip()
            pygame.time.wait(10)


xy = sonnensystem()
xy.main()