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
    so.main()  # und ausgeführt
