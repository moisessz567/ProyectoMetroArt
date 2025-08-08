class Obra:
    def __init__(self, id, titulo, autor, tipo, anio_creacion, imagen):  
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen = imagen

    def show (self):

        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")

        print(f"Tipo: {self.tipo}")
        print(f"Año de Creacion: {self.anio_creacion}")
        print(f"Imagen: {self.imagen}")

