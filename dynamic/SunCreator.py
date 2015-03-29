__author__ = 'Muhammed5, mdorfinger'

from dynamic.PlanetCreator import PlanetCreator

from dynamic.texture import TextureCreator

from OpenGL.GL import *


class SunCreator(object):
    """
    Diese Klasse xyz
    """

    __view = None
    __planet = None
    __light = None
    lightZeroPosition = []


    def __init__(self):
        """
        Diese Methode setzt Standartwerte für verwendete Variablen.
        :param anzPlanet: Die anzahl der Planeten die gezeichnet werden müssen
        :return:
        """

        self.__abstand = [10.7,16.3]
        self.__speed = [2,5]
        self.__texture = ["./textures/erde.jpg","./textures/merkur.jpg"]
        self.__anzMonde = [1,2]
        self.__planetSize = [0.91,0.49]

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
            :param zaehler: die variable zaehler sorgt dafür dass die Planet sich auch drehen und nicht an einer stelle stehen bleiben
            :return:
            """
            if isinstance(planetData[0], int):
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