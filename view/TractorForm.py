from .VehicleForm import VehicleForm
from ..model.Tractor import Tractor
from ..utils.Charge_capacity import Charge_capacity
from ..utils.Fuel_type import Fuel_type

class TractorForm(VehicleForm):
    def build_fields(self):
        self.brand_var = self._entry(0, "Marca")
        self.price_var = self._entry(1, "Precio")
        self.ac_var = self._checkbox(2, "Aire acondicionado")
        self.fuel_var = self._enum_combobox(3, "Combustible", Fuel_type, Fuel_type.DIESEL)
        self.charge_var = self._enum_combobox(4, "Capacidad de carga", Charge_capacity, Charge_capacity.HEAVY)

    def get_vehicle(self):
        return Tractor(
            charge_capacity=Charge_capacity[self.charge_var.get()],
            fuel=Fuel_type[self.fuel_var.get()],
            brand=self.brand_var.get(),
            has_air_conditioning=self.ac_var.get(),
            price=float(self.price_var.get() or 0),
        )