from tkinter import Tk , Menu, Canvas, BOTH, IntVar, Frame, Label, Entry, ttk

from lesformesgeo import Dessin, Cercle, Point, Rectangle

from lethread import ThInjecteur

class MainWin(Tk):
    
    def __init__(self):
        super().__init__()
        self._canvas = None
        self._taskbar = None
        self._nomDessin = None
        self._nextType = IntVar() # (value=1) permettrait de mettre la valeur 1 (le cercle) par defaut en lancant l'appli
        self._listeDessin = None
        self._dessin = Dessin() # importé de notre librairie
        self.configureWindow()
        self.configureMenu()
        self.configureTaskBar()
        self.configureCanvas()
        self._offset = 100
        self._threadI = ThInjecteur(self._dessin)


    def configureWindow(self):
        self.geometry("500x500")
        self.title("MainWindow")


    def configureMenu(self):
        menuRoot = Menu(self)
        menuFichier = Menu(menuRoot, tearoff=0)
        menuAction = Menu(menuRoot, tearoff=0)

        menuFichier.add_command(label="Load CSV", command=self.doLoadCSV)
        menuFichier.add_command(label="Load XML", command=self.doLoadXML)
        menuFichier.add_command(label="Save CSV", command=self.doSaveCSV)
        menuFichier.add_command(label="Save XML", command=self.doSaveXML)
        menuFichier.add_separator()
        menuFichier.add_command(label="Exit", command=self.doExit)
        menuRoot.add_cascade(label="Fichier", menu=menuFichier)

        menuAction.add_command(label="New Cercle", command=self.doNewCercle)
        menuAction.add_command(label="New Rectangle", command=self.doNewRectangle)
        menuAction.add_separator()
        menuAction.add_radiobutton(label="Next Cercle", variable = self._nextType, value=1)
        menuAction.add_radiobutton(label="Next Rectangle",variable = self._nextType, value=2)
        menuAction.add_separator()
        menuAction.add_command(label="Start Thread", command=self.doStart)
        menuAction.add_command(label="Stop Thread", command=self.doStop)
        menuAction.add_command(label="Clean", command=self.doClean)
        menuRoot.add_cascade(label="Action", menu=menuAction)
        
        self.config(menu=menuRoot)


    def doStart(self):
        if not self._threadI.is_alive():
            self._threadI.start()
    def doStop(self):
        if self._threadI.is_alive():
            self._threadI.stopThread = True
            


    def configureTaskBar(self):
        self._taskbar = Frame(self, height=50, bg='blue', width=500)
        self._taskbar.grid(column=0, row=0, sticky='ew')

        self._nomDessin = Entry(self._taskbar)
        lbName = Label(self._taskbar, text = 'Nom du dessin')
        lbName.grid(row=0, column=0, sticky='w')
        self._nomDessin.grid(row=0, column=1, sticky="w")

        lbZoneDeroulante = Label(self._taskbar, text="Dessins")
        self._listeDessin = ttk.Combobox(self._taskbar)
        lbZoneDeroulante.grid(row=0, column=2, sticky='w')
        self._listeDessin.grid(row=0, column=3, sticky='w')

        

    def configureCanvas(self):
        self._canvas = Canvas(self, bg="red")
        self._canvas.grid(column=0, row=1, sticky='ewns')
        # self._canvas.pack(fill='y', expand=1)
        self._canvas.bind("<ButtonPress>", self.doClicDown)
        self._canvas.bind("<ButtonRelease>", self.doClicUp)

        # self.simulateDraw()


    def doExit(self):
        print("Query exit")
        self.quit()

    
    def doNewCercle(self):
        print("Query new cercle")
        x = self._offset
        y = self._offset
        self._dessin.addForme(Cercle(Point(x,y),100))
        self._offset +=10
        # self._dessin.displayDessin()
        self._dessin.displayDessinCanvas(self._canvas)

    
    def doNewRectangle(self):
        print("Query new rectangle")
        x = self._offset
        y = self._offset
        self._dessin.addForme(Rectangle(Point(x,y),250,300))
        self._offset +=10
        # self._dessin.displayDessin()
        self._dessin.displayDessinCanvas(self._canvas)


    def simulateDraw(self):
        self._canvas.create_oval(10,10,250,250)
        self._canvas.create_rectangle(50,50,300,300)


    def doClicDown(self, evt):
        print(f"Down {evt} X: {evt.x} Y: {evt.y} type Select {self._nextType.get()} Value: {self._nomDessin.get()}")

    
    def doClicUp(self, evt):
        print(f"Up {evt} X: {evt.x} Y: {evt.y} type Select {self._nextType.get()}")
        if self._nextType.get() == 1:
            self._dessin.addForme(Cercle(Point(evt.x,evt.y),100))

        if self._nextType.get() == 2:
            self._dessin.addForme(Rectangle(Point(evt.x,evt.y),150,200))
            
        self._dessin.displayDessinCanvas(self._canvas)

    
    def doSaveCSV(self):
        self._dessin.persistCSV(self._nomDessin.get())


    def doSaveXML(self):
        self._dessin.persistXML(self._nomDessin.get())

    
    def doLoadCSV(self):
        print("Query load CSV")
        self.doClean()
        self._dessin.loadCSV(self._nomDessin.get())
        self._dessin.displayDessinCanvas(self._canvas)


    def doLoadXML(self):
        print("Query load XML")
        self.doClean()
        self._dessin.loadXML(self._nomDessin.get())
        self._dessin.displayDessinCanvas(self._canvas)


    def doClean(self):
        self._canvas.delete("all")
        self._dessin.cleanDessin()