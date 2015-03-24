__author__ = 'mdorfinger'
from splashscreen import *
import tkinter
from sphere import *


class Start:

    """
    asdf
    """

    root = tkinter.Tk()

    s = Splashscreen(root,"./textures/splash.png",1)
    s.__enter__()
    s.__exit__()

    root.withdraw()

    xy = Sonnensystem()
    xy.main()
