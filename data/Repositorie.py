import csv


class Repositorie:
    def get_data():
        with open('datos.csv', mode='r', encoding='utf-8') as archivo:
            reader = csv.reader(archivo, delimiter=',')
            return list(reader)
    
    def write(data):
        with open('datos.csv', mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.writer(archivo, delimiter=',')
            escritor.writerows(list(data))
    
    def update():
        pass
    def delete():
        pass
    