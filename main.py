"""
from .logic.Concessionarie import Concessionarie
from .model import Car, Tractor

concesionaria = Concessionarie()
Car(brand="Toyota")
Tractor(brand="John Deere")

print(concesionaria.find(Car, Tractor))
"""
from .view import MainWindow

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()