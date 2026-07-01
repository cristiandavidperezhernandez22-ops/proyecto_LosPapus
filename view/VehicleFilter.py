from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk

class VehicleFilter(ttk.Frame, ABC):
    """Clase base para los filtros por atributo, específicos de cada tipo."""

    def __init__(self, parent):
        super().__init__(parent)
        self.build_fields()

    @abstractmethod
    def build_fields(self):
        ...

    @abstractmethod
    def matches(self, vehicle) -> bool:
        """True si el vehículo cumple los criterios seleccionados."""
        ...

    def _enum_combobox_optional(self, row, label_text, enum_class):
        ttk.Label(self, text=label_text).grid(row=row, column=0, sticky="w", padx=4, pady=2)
        var = tk.StringVar(value="Todos")
        combo = ttk.Combobox(self, textvariable=var, state="readonly",
                              values=["Todos"] + [e.name for e in enum_class])
        combo.grid(row=row, column=1, sticky="ew", padx=4, pady=2)
        return var


class NullFilter(VehicleFilter):
    """Filtro vacío, usado cuando no hay clase seleccionada (opción 'Todos')."""
    def build_fields(self):
        pass

    def matches(self, vehicle):
        return True