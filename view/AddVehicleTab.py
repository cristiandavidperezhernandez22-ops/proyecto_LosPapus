import tkinter as tk
from tkinter import ttk, messagebox

from .CarForm import CarForm
from .TruckForm import TruckForm
from .MotorbikeForm import MotorbikeForm
from .TractorForm import TractorForm

class AddVehicleTab(ttk.Frame):
    FORM_CLASSES = {
        "Car": CarForm,
        "Truck": TruckForm,
        "Motorbike": MotorbikeForm,
        "Tractor": TractorForm,
    }

    def __init__(self, parent, on_vehicle_added=None):
        super().__init__(parent)
        self.on_vehicle_added = on_vehicle_added
        self.current_form = None
        self._build()

    def _build(self):
        top = ttk.Frame(self)
        top.pack(fill="x", padx=8, pady=8)
        ttk.Label(top, text="Tipo de vehículo:").pack(side="left")

        self.type_var = tk.StringVar(value="Car")
        combo = ttk.Combobox(top, textvariable=self.type_var, state="readonly",
                              values=list(self.FORM_CLASSES.keys()))
        combo.pack(side="left", padx=6)
        combo.bind("<<ComboboxSelected>>", lambda e: self._swap_form())

        self.form_container = ttk.Frame(self)
        self.form_container.pack(fill="both", expand=True, padx=8, pady=8)

        ttk.Button(self, text="Agregar vehículo", command=self._add_vehicle).pack(pady=8)
        self._swap_form()

    def _swap_form(self):
        if self.current_form is not None:
            self.current_form.destroy()
        form_class = self.FORM_CLASSES[self.type_var.get()]
        self.current_form = form_class(self.form_container)
        self.current_form.pack(fill="both", expand=True)

    def _add_vehicle(self):
        try:
            self.current_form.get_vehicle()
        except ValueError as e:
            messagebox.showerror("Datos inválidos", str(e))
            return
        messagebox.showinfo("Listo", "Vehículo agregado correctamente.")
        if self.on_vehicle_added:
            self.on_vehicle_added()