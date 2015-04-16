__author__ = 'mdorfinger'
from splashscreen import *
import tkinter
from tkinter import messagebox
from dynamic.Display import *


class Start:

    """
    Diese Klasse startet das ganze Programm.
    """

    root = tkinter.Tk()  # tkinter braucht man für den Splashscreen

    s = Splashscreen(root, "./textures/splash.png", 2) # Splashscreen wird aufgerufen, Bild wird mitgegeben
    s.__enter__()  # Enter Methode
    s.__exit__()  # Exit Methode

    root.withdraw()  # schliesst das Tkinter Fenster, das sich automatisch öffnet

    # Diese messagebox zeigt sich bevor das Programm startet, wenn man ok klickt, startet das Programm.
    messagebox.showinfo("Steuerung", "W ... Ansicht ändern \n T ... Textur ein/aus \n F ... Licht aus \n O ... Licht an"
                        "\n Mausrad drehen ... Rein und Rauszoomen \n \n Wird auch in der Konsole gezeigt \n Linke und"
                        "Rechte Pfeiltaste ... Beschleunigung in die angegebene Richtung")

    # Da die Infobox dann für immer verschwindet, geben wir es auch in der Konsole aus. 
    print("Steuerung: \n W ... Ansicht ändern \n T ... Textur ein/aus \n F ... Licht aus \n O ... Licht an \n Mausrad"
          "drehen ... Rein und Rauszoomen \n Linke und Rechte Pfeiltaste ... Beschleunigung in die angegebene Richtung")

    so = Sonnensystem()  # Das Sonnensystem wird aufgerufen
    #die methode main wird mit drei paramtern aufgerufen im ersten Parameter
    #sind die daten der Sonne enthalten(siehe Display klasse)
    #im zweiten die Daten der PLaneten und im dritten die daten der Monde
    #die Parameter sind wie folgt strukturiert

    #Die Sonne - (größe der Sonne,
    #Der Planet - [anz,abstand zur Sonne, speed, texture, anz monde, size]
    #Der Mond - [distanz,speed,size])
    so.main(
        5,
        [3,[10.7,16.3,25],[2,5,3],["./textures/erde.jpg","./textures/merkur.jpg","./textures/erde.jpg"],[1,2,2],[0.91,0.49,2]],
        [[2.5,1.68,1],[2,5,3],[0.2,0.1,0.1]]
    )  # und ausgeführt
