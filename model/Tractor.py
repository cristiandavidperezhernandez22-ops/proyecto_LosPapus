from .Vehicle import Vehicle
from ..utils.Charge_capacity import Charge_capacity
from ..utils.Fuel_type import Fuel_type

class Tractor(Vehicle):
    __TIRE_NUMBER = 4
    __DOORS = 2
    __PASSAGERS = 2
    def __init__(self,
                 charge_capacity:Charge_capacity = Charge_capacity.HEAVY,
                 fuel:Fuel_type = Fuel_type.DIESEL,
                 brand:str ="",
                 has_air_conditioning:bool = False,
                 price:float = 0.0
                 ):
        super().__init__(Tractor.__TIRE_NUMBER, charge_capacity, fuel, Tractor.__PASSAGERS, brand, price)
        self.doors = Tractor.__DOORS
        self.has_air_conditioning = has_air_conditioning
        self.passengers