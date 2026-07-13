from model.Vehicle import Vehicle

class Concessionarie:
    def __init__(self, *vehicles: Vehicle):
        self.vehicles = list(vehicles)
        Vehicle._registry = self

    def add(self, vehicle: Vehicle):
        self.vehicles.append(vehicle)

    def remove(self, vehicle: Vehicle):
        self.vehicles.remove(vehicle)

    def find(self, *vehicle_classes):
        return [v for v in self.vehicles if isinstance(v, vehicle_classes)]

    def __len__(self):
        return len(self.vehicles)
