class Vehicle:
    def __init__(self,
                 tire_number:int,
                 charge_capacity:str,
                 fuel:str,
                 passengers:int,
                 brand:str,
                 on:bool
                 ):
        self.tire_number = tire_number
        self.charge_capacity = charge_capacity
        self.fuel = fuel
        self.passengers = passengers
        self.brand = brand
        self.on = on
    
    def start(self):
        pass

    def drive(self):
        pass

    def brake(self):
        pass

    def honk(self):
        pass