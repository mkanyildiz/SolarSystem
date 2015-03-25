__author__ = 'mdorfinger'
from splashscreen import *
import tkinter
from dynamic.sphere2 import *


class Start:

    """
    asdf
    """

    root = tkinter.Tk()

    s = Splashscreen(root, "./textures/splash.png", 2)
    s.__enter__()
    s.__exit__()

    root.withdraw()

    xy = Sonnensystem()
    xy.main()
