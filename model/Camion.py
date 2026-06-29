from .Vehicle import Vehicle
from utils.Charge_capacity import Charge_capacity
from utils.Fuel_type import Fuel_type

class Camion(Vehicle):
    def __init__(self,
                 tire_number:int = 6,
                 charge_capacity:Charge_capacity = Charge_capacity.HEAVY,
                 fuel:Fuel_type = Fuel_type.GASOLINE,
                 passengers:int = 4,
                 brand:str ="",
                 doors:int = 2,
                 trunk_capacity:float = 0.0,
                 has_air_conditioning:bool = False,
                 price:float = 0.0
                 ):
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, price)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        self.has_air_conditioning = has_air_conditioning