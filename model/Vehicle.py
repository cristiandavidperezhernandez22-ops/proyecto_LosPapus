from abc import ABC, abstractmethod
from utils import Charge_capacity, Fuel_type


class Vehicle(ABC):
    TYPE_ID: str = None
    NOMBRE_VISIBLE: str = None

    def __init__(self,
                 tire_number: int,
                 charge_capacity: Charge_capacity,
                 fuel: Fuel_type,
                 passengers: int,
                 brand: str,
                 price: float
                 ):
        self.tire_number = tire_number
        self.charge_capacity = charge_capacity
        self.fuel = fuel
        self.passengers = passengers
        self.brand = brand
        self.price = price

    def to_row(self) -> list:
        """Serializa el objeto a una fila de CSV, anteponiendo el identificador de tipo."""
        return [self.TYPE_ID] + self._campos_propios()

    @abstractmethod
    def _campos_propios(self) -> list:
        """Cada subclase devuelve SUS atributos (sin el identificador)."""
        ...

    @classmethod
    @abstractmethod
    def from_row(cls, data: list) -> "Vehicle":
        """Reconstruye el objeto desde una fila (sin el identificador)."""
        ...