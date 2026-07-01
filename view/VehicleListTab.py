import tkinter as tk
from tkinter import ttk, messagebox

from ..model import Car, Truck, Motorbike, Tractor
from .CarFilter import CarFilter
from .TruckFilter import TruckFilter
from .MotorbikeFilter import MotorbikeFilter
from .TractorFilter import TractorFilter
from .VehicleFilter import NullFilter

class VehicleListTab(ttk.Frame):
    CLASS_OPTIONS = {
        "Todos": (None, NullFilter),
        "Car": (Car, CarFilter),
        "Truck": (Truck, TruckFilter),
        "Motorbike": (Motorbike, MotorbikeFilter),
        "Tractor": (Tractor, TractorFilter),
    }

    def __init__(self, parent, concessionarie):
        super().__init__(parent)
        self.concessionarie = concessionarie
        self.current_filter = None
        self._vehicle_by_id = {}
        self._build()
        self.refresh()

    def _build(self):
        top = ttk.Frame(self)
        top.pack(fill="x", padx=8, pady=8)
        ttk.Label(top, text="Filtrar por clase:").pack(side="left")

        self.class_var = tk.StringVar(value="Todos")
        combo = ttk.Combobox(top, textvariable=self.class_var, state="readonly",
                              values=list(self.CLASS_OPTIONS.keys()))
        combo.pack(side="left", padx=6)
        combo.bind("<<ComboboxSelected>>", lambda e: self._swap_filter())

        ttk.Button(top, text="Aplicar filtro", command=self.refresh).pack(side="left", padx=6)
        ttk.Button(top, text="Eliminar seleccionado", command=self._delete_selected).pack(side="right")

        self.filter_container = ttk.Frame(self)
        self.filter_container.pack(fill="x", padx=8, pady=4)

        columns = ("clase", "marca", "precio")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        for col, text in zip(columns, ("Clase", "Marca", "Precio")):
            self.tree.heading(col, text=text)
        self.tree.pack(fill="both", expand=True, padx=8, pady=8)

        self._swap_filter()

    def _swap_filter(self):
        if self.current_filter is not None:
            self.current_filter.destroy()
        _, filter_class = self.CLASS_OPTIONS[self.class_var.get()]
        self.current_filter = filter_class(self.filter_container)
        self.current_filter.pack(fill="x")

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        vehicle_class, _ = self.CLASS_OPTIONS[self.class_var.get()]

        vehicles = self.concessionarie.vehicles if vehicle_class is None \
            else self.concessionarie.find(vehicle_class)

        vehicles = [v for v in vehicles if self.current_filter.matches(v)]

        self._vehicle_by_id = {}
        for v in vehicles:
            iid = str(id(v))
            self._vehicle_by_id[iid] = v
            self.tree.insert("", "end", iid=iid,
                              values=(type(v).__name__, v.brand, v.price))

    def _delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Nada seleccionado", "Selecciona un vehículo de la lista primero.")
            return
        for iid in selected:
            vehicle = self._vehicle_by_id.get(iid)
            if vehicle:
                self.concessionarie.remove(vehicle)
        self.refresh()