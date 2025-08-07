class Departamentos:

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        

    def show (self):
        print(f"Id del departamento: {self.id}")
        print(f"Nombre del departamento: {self.nombre}")