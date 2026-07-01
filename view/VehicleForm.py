from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

class VehicleForm(ttk.Frame, ABC):
    """Clase base para los formularios de creación de vehículos.
    Cada subclase define sus propios campos y sabe cómo construir
    su instancia de Vehicle correspondiente."""

    def __init__(self, parent):
        super().__init__(parent)
        self.build_fields()

    @abstractmethod
    def build_fields(self):
        """Crea y posiciona los widgets de entrada específicos de este tipo."""
        ...

    @abstractmethod
    def get_vehicle(self):
        """Lee los valores actuales de los widgets y crea la instancia
        del vehículo correspondiente."""
        ...

    def _enum_combobox(self, row, label_text, enum_class, default):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky="w", padx=4, pady=2)
        var = tk.StringVar(value=default.name)
        combo = ttk.Combobox(self, textvariable=var, state="readonly",
                              values=[e.name for e in enum_class])
        combo.grid(row=row, column=1, sticky="ew", padx=4, pady=2)
        return var

    def _entry(self, row, label_text, default=""):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky="w", padx=4, pady=2)
        var = tk.StringVar(value=str(default))
        ttk.Entry(self, textvariable=var).grid(row=row, column=1, sticky="ew", padx=4, pady=2)
        return var

    def _checkbox(self, row, label_text, default=False):
        var = tk.BooleanVar(value=default)
        ttk.Checkbutton(self, text=label_text, variable=var).grid(
            row=row, column=0, columnspan=2, sticky="w", padx=4, pady=2)
        return var