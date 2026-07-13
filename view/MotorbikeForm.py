from .VehicleForm import VehicleForm
from model.Motorbike import Motorbike
from utils.Charge_capacity import Charge_capacity
from utils.Fuel_type import Fuel_type

class MotorbikeForm(VehicleForm):
    def build_fields(self):
        self.brand_var = self._entry(0, "Marca")
        self.price_var = self._entry_validado(1, "Precio")
        self.passengers_var = self._entry_validado(2, "Pasajeros", default=2)
        self.fuel_var = self._enum_combobox(3, "Combustible", Fuel_type, Fuel_type.GASOLINE)
        self.charge_var = self._enum_combobox(4, "Capacidad de carga", Charge_capacity, Charge_capacity.LIGHT)

    def get_vehicle(self):
        return Motorbike(
            charge_capacity=Charge_capacity[self.charge_var.get()],
            fuel=Fuel_type[self.fuel_var.get()],
            passengers=int(self.passengers_var.get() or 0),
            brand=self.brand_var.get(),
            price=float(self.price_var.get() or 0),
        )