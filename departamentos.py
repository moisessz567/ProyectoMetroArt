class Departamentos:

    def __init__(self, id, nombre, obra):
        self.id = id
        self.nombre = nombre
        self.obra = obra

    def show (self):
        print(f"Id del departamento: {self.id}")
        print(f"Nombre del nombre: {self.nombre}")