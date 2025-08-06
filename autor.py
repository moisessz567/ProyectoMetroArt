class Autor:
    def __init__(self, id, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.id = id
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
    
    def show(self):
        print(f"Nombre del Autor: {self.nombre}")
        print(f"Nacionalidad del Autor: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_muerte}")
