# création de notre objet Point
class Point:

    # Self réfère à l'objet Point, x et y sont les paramètres de Point
    def __init__(self, px=0, py=0):
        print("Constructeur de Point") # ini permet de construire Point
        self.x = px
        self.y = py
        if type(px) != int:
            return "Ce n est pas un int"
    
    # on veut faire apparaitre le point avec les valeurs x et y
    def display(self):
        print(f"x: {self.x} Y: {self.y}")

    def move(self, newX, newY):
        self.x = newX
        self.y = newY


class Point3D(Point): # création d'une nouvelle classe qui récupère toutes les infos de Point (héritage)
        def __init__(self, px, py, pz):
            print("Constructeur de Point3D")
            Point.__init__(self, px, py) # rappel de constructeur de la class mère*
            self.z = pz
    
        def display(self):
            print(f"X: {self.x} Y: {self.y} Z: {self.z}")


class Ligne:

    def __init__(self, p1, p2): # P1 est le point debut et P2 le point de fin de la ligne
        print("Constructeur de Ligne")
        self.pDebut = p1
        self.pFin = p2

    def display(self):
        print(f"Debut X: {self.pDebut.x} Y: {self.pDebut.y} Fin X: {self.pFin.x} Y: {self.pFin.y}") # chaque point a un x et un y pour les placer (coordonnées)
