__author__ = 'mdorfinger'


import tkinter
import time


class Splashscreen:

    """
    Diese Klasse zeigt vor Start des Programms ein Bild, das automatisch wieder verschwindet.
    """

    def __init__(self, root, file, wait):
        """
        Diese Methode initialisiert die Parametet.

        :param root: tkinter muss übergeben werden
        :param file: das Bild das angezeigt wird
        :param wait: die Zeit wielange das Bild angezeigt wird
        :return:
        """
        self.__root = root  # tkinter wird übergeben
        self.__file = file  # das bild wird übergeben
        self.__wait = wait + time.clock()  # aktuelle Zeit plus die aktuelle Zeit (damit es sich nach einer gewissen
        # Zeit wieder schließt

    def __enter__(self):
        """
        Diese Methode sorgt dafür, dass das Bild angezeigt wird
        :return:
        """
        self.__root.withdraw()  # versteckt tkinter

        # Erstellt die Componenten vom Splashscreen
        window = tkinter.Toplevel(self.__root)
        canvas = tkinter.Canvas(window)
        splash = tkinter.PhotoImage(master=window, file=self.__file)

        # Bekommt die Höhe und Breite vom Fenster
        scrW = window.winfo_screenwidth()
        scrH = window.winfo_screenheight()

        # Bekommt die Höhe und Breite vom Bild
        imgW = splash.width()
        imgH = splash.height()

        #Positioniert den Splashscreen
        Xpos = (scrW - imgW) // 2
        Ypos = (scrH - imgH) // 2

       # Window wird erstellt das das Bild zeigt
        window.overrideredirect(True)
        window.geometry('+{}+{}'.format(Xpos, Ypos))

        # Canvas wird erstellt auf dem das Bild gezeichnet wird
        canvas.configure(width=imgW, height=imgH, highlightthickness=0)
        canvas.grid()

        # Zeigt den Splashscreen auf dem Monitor
        canvas.create_image(imgW // 2, imgH // 2, image=splash)
        window.update()

        # Man speichert die Variablen um sie später gut zu löschen.
        self.__window = window
        self.__canvas = canvas
        self.__splash = splash

    def __exit__(self):
        """
        Diese Methode sorgt dafür, dass sich das Bild nach einer gewissen Zeit wieder schließt.
        :return:
        """
        now = time.clock()  # die aktuelle Zeit wird hier gespeichert
        if now < self.__wait:  # solange die aktuelle Zeit kleiner ist als (aktuelle Zeit+Wartezeit)
            time.sleep(self.__wait - now) # in dieser Zeit ist wartet das Programm (psst, es schläft)
        # Free used resources in reverse order.
        del self.__splash  # Splash wird gelöscht
        self.__canvas.destroy()  # Cancas wird gelöscht
        self.__window.destroy()  # Window wird gelöscht

        # Gibt die Kontrolle zurück zum root Programm
        self.__root.update_idletasks()
        self.__root.deiconify()
