import csv
class Repositorie:
    @staticmethod
    def get_data() -> list:
        with open("datos.csv", mode="r", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=",")
            return list(reader)
    @staticmethod
    def write(data:list):
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
            escritor.writerows(data)
    @staticmethod
    def overwrite(data: list):
        with open("datos.csv", mode="w", newline="", encoding="utf-8") as file:
            escritor = csv.writer(file, delimiter=",")
            escritor.writerows(data)
    @staticmethod
    def update(index: int, changes: list):
        data = Repositorie.get_data()
        data[index] = changes
        Repositorie.overwrite(data)
    @staticmethod
    def delete(index: int):
        data = Repositorie.get_data()
        del data[index]
        Repositorie.overwrite(data)
    @staticmethod
    def delete_all():
        open("datos.csv", mode="w", newline="", encoding="utf-8").close()