import csv
from lesobjets import Point
from xml.dom import minidom
from tkinter import Canvas


class MaxSizeException(Exception):
    """
    C'est la classe d'exception de taille max Dessin
    """
    def __init__(self, sizeMax):
        super().__init__() # call ctr classe mère
        self.sizeMax = sizeMax


    def __str__(self):
        return f"Instance de type MaxSizeException avec max: {self.sizeMax}"


class FormeGeo:
    None


class Cercle(FormeGeo): # definition d'une classe Cercle avec un point d'ancrage (x)et (y) et un rayon 
    def __init__(self, pAncrage, pRayon):
        self.ancrage = pAncrage
        self.rayon = pRayon

    
    def afficheforme(self):
        print(f"X: {self.ancrage.x} Y: {self.ancrage.y} Z: {self.rayon}")


    def afficheFormeCanvas(self, canvas:Canvas):
        x0 = self.ancrage.x - self.rayon
        y0 = self.ancrage.y - self.rayon
        x1 = self.ancrage.x + self.rayon
        y1 = self.ancrage.y + self.rayon
        canvas.create_oval(x0, y0, x1, y1)


    def toCSV(self, writer):
        tempRowCSV = ["Cercle", self.ancrage.x, self.ancrage.y, self.rayon, 0]
        writer.writerow(tempRowCSV)


    def toXML(self, parent, root):
        cercleXML = root.createElement('cercle')
        cercleXML.setAttribute('x', f"{self.ancrage.x}")
        cercleXML.setAttribute('y', f"{self.ancrage.y}")
        cercleXML.setAttribute('rayon', f"{self.rayon}")
        parent.appendChild(cercleXML)


    def toDico(self):
        dicoTemp = {}
        dicoTemp["type"] = "Cercle"
        dicoTemp["ancrage"] = {}
        dicoTemp["ancrage"]["x"] = self.ancrage.x
        dicoTemp["ancrage"]["y"] = self.ancrage.y
        dicoTemp["rayon"] = self.rayon
        return dicoTemp


class Rectangle(FormeGeo): # definition d'une classe Rectangle avec un point d'ancrage (x) et(y), une hauteur et une largeur 
    def __init__(self, pAncrage, pHauteur, pLargeur):
        self.ancrage = pAncrage
        self.hauteur =pHauteur
        self.largeur = pLargeur

    
    def afficheforme(self):
        print(f"X: {self.ancrage.x} Y: {self.ancrage.y} hauteur: {self.hauteur} largeur: {self.largeur}")


    def afficheFormeCanvas(self, canvas:Canvas):
        x0 = self.ancrage.x
        y0 = self.ancrage.y
        x1 = self.ancrage.x + self.largeur
        y1 = self.ancrage.y + self.hauteur
        canvas.create_rectangle(x0, y0, x1, y1)


    def toCSV(self, writer):
        tempRowCSV = ["Rectangle", self.ancrage.x, self.ancrage.y, self.hauteur, self.largeur]
        writer.writerow(tempRowCSV)

    
    def toXML(self, parent, root):
        rectangleXML = root.createElement('rectangle')
        rectangleXML.setAttribute('x', f"{self.ancrage.x}")
        rectangleXML.setAttribute('y', f"{self.ancrage.y}")
        rectangleXML.setAttribute('hauteur', f"{self.hauteur}")
        rectangleXML.setAttribute('largeur', f"{self.largeur}")
        parent.appendChild(rectangleXML)


    def toDico(self):
        dicoTemp = {}
        dicoTemp["type"] = "Rectangle"
        dicoTemp["ancrage"] = {}
        dicoTemp["ancrage"]["x"] = self.ancrage.x
        dicoTemp["ancrage"]["y"] = self.ancrage.y
        dicoTemp["hauteur"] = self.hauteur
        dicoTemp["largeur"] = self.largeur
        return dicoTemp


class Dessin:
    
    def __init__(self, sizeMax=100): 
        self.tableauFormeGeo =[] # pour chaque dessin, on créé un tableau (liste) pour y stocker les coordonnées des formes
        self._sizeMax = sizeMax

 
    def addForme(self, forme : FormeGeo):
        if type(forme) == Cercle:
            print("Insertion d'un cercle")
        if type(forme) == Rectangle:
            print("Insertion d'un rectangle")

        # if type(forme) != Cercle and type(forme) != Rectangle:
        #    print(f"{type(forme)} non supporte")
        #    return

        if not isinstance(forme, FormeGeo):
            print(f"{type(forme)} non supporte (heritage)")
            return


        if len(self.tableauFormeGeo) < self._sizeMax:
            self.tableauFormeGeo.append(forme)
            # return True
        else:
            # return False
            raise MaxSizeException(self._sizeMax)


    def displayDessin(self):
        for fg in self.tableauFormeGeo:
            fg.afficheforme()


    def displayDessinCanvas(self, canvas:Canvas):
        for fg in self.tableauFormeGeo:
            fg.afficheFormeCanvas(canvas)


    def persistCSV(self, nomFichier): # nomFichier= "leDessin" - le nomFichier est "leDessin" par défaut si aucun nom de fichier n'est renseigné lorsqu'on sauvegarde
        if len(nomFichier)==0:
            return
        
        with open(f"{nomFichier}.csv", "w", newline="") as handleFileWrite:
            writer = csv.writer(handleFileWrite)
            # mise en place du header csv
            tabHeader = ["Type", "X", "Y", "DC1", "DC2"]
            writer.writerow(tabHeader)
            for fg in self.tableauFormeGeo: # on écrit les formes dans le fichier
                fg.toCSV(writer)


    def persistXML(self, nomFichier):
        if len(nomFichier)==0:
            return
        
        root = minidom.Document()
        xml = root.createElement('dessin') 
        root.appendChild(xml)        
        # TODO gestion des formes
        for fg in self.tableauFormeGeo: # on écrit les formes dans le fichier
                fg.toXML(xml, root  )
        xml_str = root.toprettyxml(indent ="\t")
        with open(f"{nomFichier}.xml", "w") as handleXMLFile:
            handleXMLFile.write(xml_str)

    def cleanDessin(self):
        self.tableauFormeGeo=[]


    def createCerclesFromXML(self, tabCercle):
        for cercleXML in tabCercle:
            x = int(cercleXML.getAttribute("x"))
            y = int(cercleXML.getAttribute("y"))
            rayon = int(cercleXML.getAttribute("rayon"))
            tempCercle = Cercle(Point(x,y), rayon)
            self.addForme(tempCercle)

    def createRectanglesFromXML(self, tabRectangle):
        for rectangleXML in tabRectangle:
            x = int(rectangleXML.getAttribute("x"))
            y = int(rectangleXML.getAttribute("y"))
            hauteur = int(rectangleXML.getAttribute("hauteur"))
            largeur = int(rectangleXML.getAttribute("largeur"))
            tempRectangle = Rectangle(Point(x,y), hauteur, largeur)
            self.addForme(tempRectangle)


    def loadXML(self, nomFichier):
        if len(nomFichier)==0:
            return
        self.cleanDessin()
        rootDocXml = minidom.parse(f"{nomFichier}.xml") # lecture et parse du fichier
        # recherche des cercles
        tabCercle = rootDocXml.getElementsByTagName("cercle")
        self.createCerclesFromXML(tabCercle)
        # recherche des rectangles
        tabRectangle = rootDocXml.getElementsByTagName("rectangle")
        self.createRectanglesFromXML(tabRectangle)


    def loadCSV(self,nomFichier):
        if len(nomFichier)==0:
            return
        
        self.cleanDessin()
        with open(f"{nomFichier}.csv", newline='') as csvfile:
            formeGeoReader = csv.reader(csvfile,delimiter=',')
            compteurRow = 0
            for row in formeGeoReader:
                print(row)
                if compteurRow != 0:
                    if row[0] == "Cercle":
                        # création d'un cercle
                        tempCercle = Cercle(Point(int(row[1]), int(row[2])), int(row[3]))
                        self.addForme(tempCercle)
                    if row[0] == "Rectangle":
                        # création d'un rectangle
                        tempRectangle = Rectangle(Point(int(row[1]), int(row[2])), int(row[3]), int(row[4]))
                        self.addForme(tempRectangle)
                compteurRow +=1


    def toFormDico(self):
        arrayForms = []
        for form in self.tableauFormeGeo:
            dicoTemp = form.toDico()
            arrayForms.append(dicoTemp)
        return arrayForms