from .VehicleForm import VehicleForm
from model.Truck import Truck
from utils.Charge_capacity import Charge_capacity
from utils.Fuel_type import Fuel_type

class TruckForm(VehicleForm):
    def build_fields(self):
        self.brand_var = self._entry(0, "Marca")
        self.price_var = self._entry_validado(1, "Precio")
        self.tire_var = self._entry_validado(2, "Número de llantas", default=6)
        self.passengers_var = self._entry_validado(3, "Pasajeros", default=4)
        self.doors_var = self._entry_validado(4, "Puertas", default=2)
        self.trunk_var = self._entry_validado(5, "Capacidad de carga (m³)", default=0.0)
        self.ac_var = self._checkbox(6, "Aire acondicionado")
        self.fuel_var = self._enum_combobox(7, "Combustible", Fuel_type, Fuel_type.GASOLINE)
        self.charge_var = self._enum_combobox(8, "Capacidad de carga", Charge_capacity, Charge_capacity.HEAVY)

    def get_vehicle(self):
        return Truck(
            tire_number=int(self.tire_var.get() or 0),
            charge_capacity=Charge_capacity[self.charge_var.get()],
            fuel=Fuel_type[self.fuel_var.get()],
            passengers=int(self.passengers_var.get() or 0),
            brand=self.brand_var.get(),
            doors=int(self.doors_var.get() or 0),
            trunk_capacity=float(self.trunk_var.get() or 0),
            has_air_conditioning=self.ac_var.get(),
            price=float(self.price_var.get() or 0),
        )