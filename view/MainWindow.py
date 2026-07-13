import tkinter as tk
from tkinter import ttk

from logic.Concessionarie import Concessionarie
from .AddVehicleTab import AddVehicleTab
from .VehicleListTab import VehicleListTab

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Concesionaria LosPapus")
        self.geometry("640x480")

        self.concessionarie = Concessionarie()

        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True)

        self.list_tab = VehicleListTab(notebook, self.concessionarie)
        add_tab = AddVehicleTab(notebook, on_vehicle_added=self.list_tab.refresh)

        notebook.add(add_tab, text="Agregar vehículo")
        notebook.add(self.list_tab, text="Vehículos")