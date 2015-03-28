

__author__ = 'Muhammed5, mdorfinger'


from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from PIL.Image import *

class TextureCreator(object):
    __view = None

    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """

        self.txtmerkur = None
        self.txterde = None
        self.txtsonne = None
        self.txtmond = None
        self.mod = True
        self.var = False
        # self.__view = Sonnensystem()


    def loadTexture(self, bild):
        """
        Diese Methode lädt die Texturen, die auf die Planeten gegeben werden
        :param bild: den Pfad auf das bild welches man verwenden möchte
        :return: die Textur ID
        """
        try:
            image = open(bild)
            self.var = True
        except:
            print ("Unable to load image")
        # Textur
        if self.var == True:
            ix = image.size[0] # Größe der Textur (Horizontal)
            iy = image.size[1] # Größe der Textur (Vertikal)
            image = image.tostring("raw", "RGBX", 0, -1)

            # Textur erstellen
            #glEnable(GL_TEXTURE_2D)
            textures = glGenTextures(1) # Textur ID
            glBindTexture(GL_TEXTURE_2D, textures)  # 2D Textur (x and y Größe)

            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_NEAREST)
            gluBuild2DMipmaps(GL_TEXTURE_2D, 3, ix, iy, GL_RGBA, GL_UNSIGNED_BYTE, image)

            return textures # ID wird zurückgegeben

    def sphere(self, radius, txt):
        """
        Diese Methode erstellt eine Sphere und legt eine Texur darauf.
        :param radius: Der Radius der Sphere
        :param txt: die Textur die auf die Sphere gelegt werden soll
        :return:
        """

        quadratic = gluNewQuadric()

        gluQuadricNormals(quadratic, GLU_SMOOTH)  # Create Smooth Normals (NEW)
        gluQuadricTexture(quadratic, GL_TRUE)  # Create Texture Coords (NEW)
        #gluQuadricDrawStyle(self.sphere,GLU_LINE)

        glBindTexture(GL_TEXTURE_2D, txt)
        gluSphere(quadratic,radius,30,30)
        #glutWireSphere(2,100,20)

    def textureChange(self):
        """
        Diese Methode ändert den Zustand der Textur zwischen eingeschalten und ausgeschalten.
        :return:
        """

        if self.mod is True:
            glEnable(GL_TEXTURE_2D)
            self.mod = False

            self.txtmerkur = self.loadTexture("./textures/merkur.jpg")
            self.txtsonne = self.loadTexture("./textures/sonne.jpg")
            self.txterde = self.loadTexture("./textures/erde.jpg")
            self.txtmond  = self.loadTexture("./textures/moon.jpg")
        else:
            glDisable(GL_TEXTURE_2D)
            self.mod = True