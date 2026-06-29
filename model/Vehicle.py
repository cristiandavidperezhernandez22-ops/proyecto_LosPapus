from abc import ABC, abstractmethod
from utils import Charge_capacity
from utils import Fuel_type
class Vehicle:
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
