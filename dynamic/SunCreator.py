__author__ = 'mkanyildiz, mdorfinger'

from dynamic.PlanetCreator import PlanetCreator

from dynamic.texture import TextureCreator

from OpenGL.GL import *


class SunCreator(object):
    """
    Diese Klasse SunCreator beinhaltet methoden zum erstellen der Sonne und zum
    Belichten der Umgebung bzw. das Sonnenlicht.
    """

    __view = None
    __planet = None
    __light = None
    lightZeroPosition = []


    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :return:
        """

        self.__view = TextureCreator()
        self.__planet = PlanetCreator()
        self.lightZeroPosition = [0.,0.,0.,1]




    def disableLight(self):
        """
        Diese Methode deaktiviert das Licht, falls es aktiviert ist.
        :return:
        """
        glDisable(GL_LIGHTING)
        glDisable(GL_LIGHT0)


    def showLight(self):
        """
        Diese Methode aktiviert das Licht, falls es deaktiviert ist.
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

    def createSun(self,zaehler,sizeSonne,planetData,moonData):
            """
            Diese Methode xyz
            :param moonData: moonData ist ein Array der erst bei der MoonCreator KLasse aufgerufen wird. Die Liste beinhaltet variablen wie die größe des Mondes die distanz zum planeten usw.
            :param planetData: planetData ist ein Array der erst bei der PlanetCreator KLasse aufgerufen wird. Die Liste beinhaltet variablen wie die größe der Planeten die distanz zum planeten usw.
            :param sizeSonne: Die GRöße der Sonne
            :param zaehler: die variable zaehler sorgt dafür dass die Planet sich auch drehen und nicht an einer stelle stehen bleiben
            :return:
            """
            #Überprüfen on die anzahl der Planeten ein int wert ist ansonsten wird ein TypeError aufgerufen
            if isinstance(planetData[0], int):
                #ist die anzahl kleiner gleich null wird ein zerodivisionerror aufgerufen
                if planetData[0] == 0:
                    raise ZeroDivisionError("Ein Sonnensystem besteht mindestens aus einem Planeten")
                else:
                    #Sonne
                    glPushMatrix()
                    self.disableLight()

                    self.__view.txtsonne = self.__view.loadTexture("./textures/sonne.jpg")
                    glRotate(90, 1, 0, 0)#um die texuren zu fixen müssen wir unser sphere drehen
                    self.__view.sphere(sizeSonne, self.__view.txtsonne)
                    glRotate(-90, 1, 0, 0)
                    self.showLight()        # das licht wird hier aktiviert da wir das licht anstelle der Sonne haben wollen
                                            #dies geschieht dadurch indem wir die belichtung mit der sonne im push und pop erstellen
                    glPopMatrix()

                    #Hier zeichen wir N Planeten
                    for x in range(0, planetData[0]):    # die forschleife ruft je nachdem wieviel planeten wir haben wollen die Metjode createPlanet auf
                       #Die Paramter für die Methode sind wie folgt
                       # Rotationsvariable-distanz zwischen Sonne und Planet-Geschwindigkeit der drehung-die textur bez-anzahl der Monde
                        self.__planet.createPlanet(
                            zaehler,
                            planetData[1][x],
                            planetData[2][x],
                            planetData[3][x],
                            planetData[4][x],
                            planetData[5][x],
                            moonData)
            else:
                raise TypeError("Only Integer allowed")