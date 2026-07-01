from .VehicleFilter import VehicleFilter
from ..utils.Fuel_type import Fuel_type
from ..utils.Car_type import Car_type

class CarFilter(VehicleFilter):
    def build_fields(self):
        self.fuel_var = self._enum_combobox_optional(0, "Combustible", Fuel_type)
        self.car_type_var = self._enum_combobox_optional(1, "Tipo de auto", Car_type)

    def matches(self, vehicle):
        if self.fuel_var.get() != "Todos" and vehicle.fuel != Fuel_type[self.fuel_var.get()]:
            return False
        if self.car_type_var.get() != "Todos" and vehicle.car_type != Car_type[self.car_type_var.get()]:
            return False
        return True