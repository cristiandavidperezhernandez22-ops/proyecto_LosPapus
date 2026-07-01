from .Vehicle import Vehicle
from ..utils import Charge_capacity, Fuel_type

class Motorbike(Vehicle):
    def __init__(self,
                 tire_number:int = 2,
                 charge_capacity:Charge_capacity = Charge_capacity.LIGHT,
                 fuel:Fuel_type = Fuel_type.GASOLINE,
                 passengers:int = 2,
                 brand:str = "",
                 price:float = 0.0):
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, price)
        