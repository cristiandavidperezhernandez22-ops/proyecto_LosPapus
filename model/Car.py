from .Vehicle import Vehicle
from utils.Charge_capacity import Charge_capacity

class Car(Vehicle):
    def __init__(self,
                 tire_number:int = 0,
                 charge_capacity:Charge_capacity = Charge_capacity.MEDIUM,
                 fuel:str = "",
                 passengers:int = 0,
                 brand:str ="",
                 doors:int = 0,
                 trunk_capacity:float = 0.0,
                 has_air_conditioning:bool = False,
                 price:float = 0.0
                 ):
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, price)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        self.has_air_conditioning = has_air_conditioning

    def honk(self) -> None:
        print("Beep beep!")

