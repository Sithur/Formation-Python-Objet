#!/usr/bin/env python

import sys
from mainwin import MainWin
from lesobjets import Point
from lesformesgeo import Cercle, Rectangle, Dessin, MaxSizeException
from lethread import ThInjecteur

def Main():
    leDessin = Dessin() # création du dessin

    unCercle = Cercle(Point(100,200), 300) # création d'un cercle
    unAutreCercle = Cercle(Point(1000,2000), 3000) # création d'un autre cercle
    unRectangle = Rectangle(Point(1,2), 123, 456)
    

    try:
        leDessin.addForme(unCercle) # ajout d'un cercle au dessin
        leDessin.addForme(unRectangle)
        leDessin.addForme(unAutreCercle) # ajout d'un autre cercle au dessin    
        leDessin.addForme(unRectangle)
    except MaxSizeException as ex:
        #print(f"max: {ex.sizeMax}")
        print(ex)
    except Exception as ez:
        print("Autre erreur")



    leDessin.displayDessin() #affichage du dessin
    leDessin.persistCSV()
    leDessin.persistXML()


def MainGUI():
    mainWin = MainWin()
    mainWin.mainloop()
    print("Fin app")




if __name__ == "__main__":
    if len(sys.argv) < 2:
        Main()
    else:
        if sys.argv[1] == "GUI":
            # thInjecteur = ThInjecteur()  creation de l'instance du thread
            # thInjecteur.setDaemon(True)
            # thInjecteur.start() # start du thread
            MainGUI()
            # thInjecteur.stopThread = True
            # print("Attente fin de thread")
            # thInjecteur.join(5)
            # print(f"Fin de thread notifie status {thInjecteur.is_alive()}")
        else:
            Main()



# pour lancer l'environnement venv : .\venv\Scripts\activate.ps1