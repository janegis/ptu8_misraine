from tkinter import *
from apps.destytojas import Destytojas
from apps.monika import Studente
from apps.igno_app import IgnoApp
from apps.giedrius import Giedrius
from apps.lina import Lina
from apps.donatas import Donatas

class MainApp():
    def __init__(self, main):
        self.main = main
        self.f_catalog = Frame(self.main)
        self.l_pasirinkimai = Label(self.f_catalog, text="Pasirinkite")
        self.b_destytojas = Button(self.f_catalog, text="Destytojas", command=self.run_destytojas)
        self.b_giedrius = Button(self.f_catalog, text="Giedrius", command=self.run_giedrius)
        self.b_ignas = Button(self.f_catalog, text="Ignas",command=self.run_ignas)
        self.b_lina = Button(self.f_catalog, text="Lina", command=self.run_lina)
        self.b_studente = Button(self.f_catalog, text='Monika', command=self.run_studente)
        self.b_donatas = Button (self.f_catalog, text='Donatas', command=self.run_donatas)
        
        self.l_pasirinkimai.pack(side=TOP)
        self.b_donatas.pack()
        self.b_destytojas.pack()
        self.b_ignas.pack()
        self.b_giedrius.pack()
        self.b_lina.pack()
        self.b_studente.pack()
        self.f_catalog.pack()
        
    def run_destytojas(self):
        self.window_destytojas = Toplevel(self.main)
        self.app = Destytojas(self.window_destytojas)

    def run_studente(self):
        self.window_studente = Toplevel(self.main)
        self.app2 = Studente(self.window_studente)

    def run_ignas(self):
        self.window_my_app = Toplevel(self.main)
        self.app = IgnoApp(self.window_my_app)

    def run_giedrius(self):
        self.window_giedrius = Toplevel(self.main)
        self.app = Giedrius(self.window_giedrius)

    def run_lina(self):
        self.window_lina = Toplevel(self.main)
        self.app = Lina(self.window_lina)

    def run_donatas(self):
        self.window_donatas = Toplevel(self.main)
        self.app = Donatas(self.window_donatas)
