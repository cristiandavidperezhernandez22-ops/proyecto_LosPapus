from .VehicleFilter import VehicleFilter
from ..utils.Fuel_type import Fuel_type

class MotorbikeFilter(VehicleFilter):
    def build_fields(self):
        self.fuel_var = self._enum_combobox_optional(0, "Combustible", Fuel_type)

    def matches(self, vehicle):
        return self.fuel_var.get() == "Todos" or vehicle.fuel == Fuel_type[self.fuel_var.get()]