import threading
import time
from lesformesgeo import Dessin, Cercle, Point


class ThInjecteur(threading.Thread):
    
    def __init__(self, dessin : Dessin):
        super().__init__()
        self.stopThread = False
        self._dessin = dessin
        self._xy = 15


    def innerProcess(self):
        # for cpt in range(0,500):
        #    print(f"Thread cpt {cpt}")
        #   time.sleep(1) # à ne pas utiliser (seulement pour exemple)
        #    if self.stopThread:
        #        break

        while not self.stopThread:
            cercle = Cercle(Point(self._xy,self._xy), 15) # creation d'une instance
            self._xy += 5
            if self._xy >= 200:
                self._xy = 20
            
            self._dessin.addForme(cercle)
            time.sleep(5)


    def run(self):
        self.innerProcess()
