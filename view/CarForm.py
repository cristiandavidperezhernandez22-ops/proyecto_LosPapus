from .VehicleForm import VehicleForm
from model.Car import Car
from utils.Charge_capacity import Charge_capacity
from utils.Fuel_type import Fuel_type
from utils.Car_type import Car_type

class CarForm(VehicleForm):
    def build_fields(self):
        self.brand_var = self._entry(0, "Marca")
        self.price_var = self._entry_validado(1, "Precio")
        self.doors_var = self._entry_validado(2, "Puertas", default=4)
        self.trunk_var = self._entry_validado(3, "Capacidad baúl (m³)", default=0.0)
        self.ac_var = self._checkbox(4, "Aire acondicionado")
        self.fuel_var = self._enum_combobox(5, "Combustible", Fuel_type, Fuel_type.GASOLINE)
        self.charge_var = self._enum_combobox(6, "Capacidad de carga", Charge_capacity, Charge_capacity.MEDIUM)
        self.car_type_var = self._enum_combobox(7, "Tipo de auto", Car_type, Car_type.COMPACT)

    def get_vehicle(self):
        return Car(
            brand=self.brand_var.get(),
            price=float(self.price_var.get() or 0),
            doors=int(self.doors_var.get() or 0),
            trunk_capacity=float(self.trunk_var.get() or 0),
            has_air_conditioning=self.ac_var.get(),
            fuel=Fuel_type[self.fuel_var.get()],
            charge_capacity=Charge_capacity[self.charge_var.get()],
            car_type=Car_type[self.car_type_var.get()],
        )