from .Vehicle import Vehicle
from utils import Charge_capacity, Fuel_type, Car_type

class Car(Vehicle):
    def __init__(self,
                 tire_number:int = 4,
                 charge_capacity:Charge_capacity = Charge_capacity.MEDIUM,
                 fuel:Fuel_type = Fuel_type.GASOLINE,
                 passengers:int = 4,
                 brand:str ="",
                 doors:int = 4,
                 trunk_capacity:float = 0.0,
                 has_air_conditioning:bool = False,
                 price:float = 0.0,
                 car_type:Car_type = Car_type.COMPACT
                 ):
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, price)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        self.has_air_conditioning = has_air_conditioning
        self.car_type = car_type
        