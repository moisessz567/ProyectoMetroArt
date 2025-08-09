class Departamentos:

    """Clase que representa un departamento del Metropolitan Museum of Art
    
    Los departamentos corresponden a las diferentes categorías o áreas de colección 
    del museo (por ejemplo: 'Arte Europeo', 'Arte Asiático', 'Pinturas', etc.)

    Atributos:
        id (int): Identificador único del departamento según la API del Met
        nombre (str): Nombre oficial del departamento
    """

    def __init__(self, id, nombre):

        """Inicializa una instancia de Departamento
        
        Args:
            id (int): Número de identificación único del departamento
            nombre (str): Nombre descriptivo del departamento (ej. 'Arte Moderno')
        """

        self.id = id
        self.nombre = nombre
        

    def show (self):

        """Muestra en consola la información del departamento formateada
        
        Imprime:
            - ID del departamento
            - Nombre del departamento
        """

        print(f"Id del departamento: {self.id}")
        print(f"Nombre del departamento: {self.nombre}")