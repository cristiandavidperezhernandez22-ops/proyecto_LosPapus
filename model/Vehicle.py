class Vehicle:
    def __init__(self,
                 tire_number:int,
                 charge_capacity:str,
                 fuel:str,
                 passengers:int,
                 brand:str,
                 on:bool) -> None:
        self.tire_number = tire_number
        self.charge_capacity = charge_capacity
        self.fuel = fuel
        self.passengers = passengers
        self.brand = brand
        self.on = on

    def start(self) -> None:
        """Start the vehicle engine."""
        pass

    def drive(self) -> None:
        """Drive the vehicle."""
        pass

    def brake(self) -> None:
        """Apply brakes."""
        pass

    def honk(self) -> None:
        """Sound the horn."""
        pass