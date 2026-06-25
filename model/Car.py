import Vehicle

class Car(Vehicle):
    def __init__(self, tire_number:int,
                 charge_capacity:str,
                 fuel:str,
                 passengers:int,
                 brand:str,
                 on:bool,
                 doors:int,
                 trunk_capacity:float,
                 has_air_conditioning:bool)->None:
        super().__init__(tire_number, charge_capacity, fuel, passengers, brand, on)
        self.doors = doors
        self.trunk_capacity = trunk_capacity
        self.has_air_conditioning = has_air_conditioning

    def honk(self) -> None:
        print("Beep beep!")