class Autor:

    """Clase que representa a un artista/autor cuyas obras están en el Metropolitan Museum of Art.
    
    Atributos:
        nombre (str): Nombre completo del artista (ej. 'Vincent van Gogh').
        nacionalidad (str): País o región de origen del artista (ej. 'Holandés').
        fecha_nacimiento (str): Fecha de nacimiento en formato texto (ej. '1853-03-30').
        fecha_muerte (str): Fecha de fallecimiento en formato texto (ej. '1890-07-29').
                            Puede ser una cadena vacía si el artista sigue vivo.
    """

    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):

        """Inicializa una nueva instancia de Autor
        
        Argumentos:
            nombre (str): Nombre completo del artista
            nacionalidad (str): Nacionalidad u origen del artista
            fecha_nacimiento (str): Fecha de nacimiento en cualquier formato descriptivo
            fecha_muerte (str): Fecha de fallecimiento (cadena vacía si no aplica)
        """

        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte
    
    def show(self):

        """Muestra en consola la información biográfica del artista con formato legible
        
        Imprime:
            - Nombre completo
            - Nacionalidad
            - Fecha de nacimiento
            - Fecha de muerte 
        """

        print(f"Nombre del Autor: {self.nombre}")
        print(f"Nacionalidad del Autor: {self.nacionalidad}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento}")
        print(f"Fecha de muerte: {self.fecha_muerte}")
