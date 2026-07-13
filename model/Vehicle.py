from abc import ABC
from utils import Fuel_type, Charge_capacity

class Vehicle(ABC):
    _registry = None

    def __init__(self,
                 tire_number:int,
                 charge_capacity:Charge_capacity,
                 fuel:Fuel_type,
                 passengers:int,
                 brand:str,
                 price:float):
        self.tire_number = tire_number
        self.charge_capacity = charge_capacity
        self.fuel = fuel
        self.passengers = passengers
        self.brand = brand
        self.price = price

        if Vehicle._registry is not None:
            Vehicle._registry.add(self)

    def __repr__(self):
        return f"{type(self).__name__}(brand={self.brand}, price={self.price})"