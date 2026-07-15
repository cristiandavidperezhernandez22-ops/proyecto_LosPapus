from .Vehicle import Vehicle
from logic.Registry import VehicleRegistry
from utils import Charge_capacity, Fuel_type, Car_type


@VehicleRegistry.register("C", "Carro")
class Car(Vehicle):
    def __init__(self,
                 tire_number: int = 4,
                 charge_capacity: Charge_capacity = Charge_capacity.MEDIUM,
                 fuel: Fuel_type = Fuel_type.GASOLINE,
                 passengers: int = 4,
                 brand: str = "",
                 doors: int = 4,
                 trunk_capacity: float = 0.0,
                 has_air_conditioning: bool = False,
                 price: float = 0.0,
                 car_type: Car_type = Car_type.COMPACT
                 ):
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, price)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        self.has_air_conditioning = has_air_conditioning
        self.car_type = car_type

    def _campos_propios(self) -> list:
        return [
            self.tire_number,
            self.charge_capacity.value,
            self.fuel.value,
            self.passengers,
            self.brand,
            self.price,
            self.doors,
            self.trunk_capacity,
            self.has_air_conditioning,
            self.car_type.value,
        ]

    @classmethod
    def from_row(cls, data: list) -> "Car":
        return cls(
            tire_number=int(data[0]),
            charge_capacity=Charge_capacity(data[1]),
            fuel=Fuel_type(data[2]),
            passengers=int(data[3]),
            brand=data[4],
            price=float(data[5]),
            doors=int(data[6]),
            trunk_capacity=float(data[7]),
            has_air_conditioning=data[8] == "True",
            car_type=Car_type(data[9]),
        )