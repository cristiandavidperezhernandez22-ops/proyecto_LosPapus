from model import Vehicle
from model import Car

class Concessionarie:
    def __init__(self, *vehicles:Vehicle):
        self.vehicles = list(vehicles)
    
    def add(self, vehicle:Vehicle):
        self.vehicles.append(vehicle)
    
    def remove(self, vehicle:Vehicle):
        self.vehicles.remove(vehicle)
