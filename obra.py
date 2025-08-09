class Obra:
    
    """Clase que representa una obra de arte del Metropolitan Museum of Art
    
    Atributos:
        id (int): Identificador único de la obra en la API del Met
        titulo (str): Título de la obra
        autor (str): Nombre del artista que creó la obra
        tipo (str): Clasificación o tipo de obra (pintura, escultura, etc.)
        anio_creacion (str): Año o período de creación de la obra
        imagen (str): URL de la imagen en tamaño pequeño de la obra
    """
    def __init__(self, id, titulo, autor, tipo, anio_creacion, imagen):  

        """Inicializa una nueva instancia de Obra.
        
        Args:
            id (int): Identificador único de la obra.
            titulo (str): Título de la obra.
            autor (str): Nombre del artista.
            tipo (str): Clasificación de la obra.
            anio_creacion (str): Año o período de creación.
            imagen (str): URL de la imagen en tamaño pequeño.
        """

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.tipo = tipo
        self.anio_creacion = anio_creacion
        self.imagen = imagen

    def show (self):

        """Muestra en consola todos los atributos de la obra con formato.
        
        Muestra:
            - ID
            - Título
            - Autor
            - Tipo/clasificación
            - Año de creación
            - URL de la imagen
        """

        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")

        print(f"Tipo: {self.tipo}")
        print(f"Año de Creacion: {self.anio_creacion}")
        print(f"Imagen: {self.imagen}")

    def show_1 (self):

        """Muestra en consola información básica de la obra (versión reducida).
        
        Muestra solo:
            - ID
            - Título
            - Autor
        """

        print(f"ID: {self.id}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")