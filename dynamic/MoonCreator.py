__author__ = 'mkanyildiz, mdorfinger'

from OpenGL.GL import *

from dynamic.texture import TextureCreator


class MoonCreator():
    """
    Diese Klasse MoonCreator beinhaltet methoden um einen Mond herzustellen.
    Dies geschieht nur dann wenn der Benutzer Monde als Parameter angibt
    """

    __view = None

    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """
        self.__view = TextureCreator()


    def createMoon(self,zaehler,distanz,speed,size):
        """
        Diese Methode createMoon ist dafür zuständlich Monde für die Planeten zu generieren
        :param size: Die Größe des Mondes
        :param zaehler: ist für die Rotation zuständig. Bei jedem durchlauf der while schleife wird diese variable hochgezählt und der Rotationswinkel wird geändert dadurch wird das Rotieren ermöglicht
        :param distanz: distanz zwischen mond und planet
        :param speed:   geschwindigkeit der rotation um den Planeten
        :return:
        """

        #Überprüfen on die größe ein int oder ein Float wert sind ansonsten wird ein TypeError aufgerufen
        if isinstance(size, (int,float)):
            #ist die größe kleiner gleich null wird ein zerodivisionerror aufgerufen
            if size <= 0:
                raise ZeroDivisionError("Mond muss größer 0 sein")
            #Hier werden die restlichen parameter darauf überprüft ob sie den richtigen datentyp haben
            elif isinstance(distanz,(int,float)):
                if isinstance(speed,(int,float)):
                    #Moon
                    glPushMatrix()
                    color = [0.211,0.211,0.211,1.]
                    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)

                    #Rotation um den Planeten
                    glRotatef(speed* zaehler, 0, 1, 0) #zuerst wird rotiert
                    glTranslatef(-distanz, 0, 0)       # und dann um die gewünschte distanz verschoben

                    #rotation um die eigene achse
                    glRotatef(5* zaehler, 0, 1, 0)     #rotation um die eigene Achse

                    #anzeigen der texturen
                    self.__view.txtmond = self.__view.loadTexture("./textures/moon.jpg")
                    glRotate(90, 1, 0, 0)
                    self.__view.sphere(size, self.__view.txtmond)
                    glRotate(-90, 1, 0, 0)
                    glPopMatrix()
                else:
                    raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")
            else:
                raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")
        else:
            raise TypeError("ONLY INTEGER OR FLOAT VALUES ARE ALLOWED")

