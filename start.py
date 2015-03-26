__author__ = 'mdorfinger'
from splashscreen import *
import tkinter
from dynamic.sphere2 import *


class Start:

    """
    Diese Klasse startet das ganze Programm.
    """

    root = tkinter.Tk() # tkinter braucht man für den Splashscreen

    s = Splashscreen(root, "./textures/splash.png", 2) # Splashscreen wird aufgerufen, Bild wird mitgegeben
    s.__enter__() # Enter Methode
    s.__exit__() # Exit Methode

    root.withdraw() # schliesst das Tkinter Fenster, das sich automatisch öffnet

    so = Sonnensystem() # Das Sonnensystem wird aufgerufen
    so.main() # und ausgeführt
