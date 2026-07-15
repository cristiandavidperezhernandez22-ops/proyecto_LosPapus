import csv
from logic.Registry import VehicleRegistry


class Repositorie:
    @staticmethod
    def get_data() -> list:
        """Filas crudas del CSV (listas de strings), sin reconstruir objetos."""
        with open("datos.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            return list(reader)

    @staticmethod
    def get_vehicles() -> list:
        """Objetos ya reconstruidos (Car, Truck, etc.) usando el Registry."""
        filas = Repositorie.get_data()
        return [VehicleRegistry.crear_desde_fila(fila) for fila in filas if fila]

    @staticmethod
    def write(vehiculos: list):
        """Agrega uno o más vehículos nuevos al final, sin borrar lo existente."""
        filas_nuevas = [v.to_row() for v in vehiculos]
        try:
            with open("datos.csv", mode="r", encoding="utf-8") as file:
                contenido = file.read()
        except FileNotFoundError:
            contenido = ""
        jump_need = contenido != "" and not contenido.endswith("\n")
        with open("datos.csv", mode="a", newline="", encoding="utf-8") as file:
            if jump_need:
                file.write("\n")
            escritor = csv.writer(file, delimiter=",")
            escritor.writerows(filas_nuevas)

    @staticmethod
    def overwrite(vehiculos: list):
        """Reemplaza TODO el contenido del CSV con la lista de vehículos dada."""
        filas = [v.to_row() for v in vehiculos]
        with open("datos.csv", mode="w", newline="", encoding="utf-8") as file:
            escritor = csv.writer(file, delimiter=",")
            escritor.writerows(filas)

    @staticmethod
    def update(index: int, nuevo_vehiculo):
        vehiculos = Repositorie.get_vehicles()
        vehiculos[index] = nuevo_vehiculo
        Repositorie.overwrite(vehiculos)

    @staticmethod
    def delete(index: int):
        vehiculos = Repositorie.get_vehicles()
        del vehiculos[index]
        Repositorie.overwrite(vehiculos)

    @staticmethod
    def delete_all():
        open("datos.csv", mode="w", newline="", encoding="utf-8").close()