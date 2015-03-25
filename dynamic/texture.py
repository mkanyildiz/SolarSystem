

__author__ = 'Muhammed5'


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import *

class TextureCreator(object):
    __view = None

    def __init__(self):

        self.txtmerkur = None
        self.txterde = None
        self.txtsonne = None
        self.txtmond = None
        self.mod = True
        #self.__view = Sonnensystem()


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
        gluSphere(quadratic,radius,30,30)
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