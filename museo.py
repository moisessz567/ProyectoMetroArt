from departamentos import Departamentos
from obra import Obra
from autor import Autor
from API import obtener_departamentos
from Csv_Reader import mostrar_nacionalidades

class Museo:

    """Clase principal que representa el sistema de gestión del Metropolitan Museum of Art
    
    Esta clase permite interactuar con la API del Met para:
    - Explorar departamentos
    - Buscar obras por diferentes criterios
    - Mostrar detalles completos de obras
    - Gestionar información de artistas
    
    Atributos:
        apidepartamentos (dict): Datos crudos de departamentos desde la API
        departamento (list[Departamentos]): Lista de objetos departamento
        obras (list[Obra]): Lista de obras cargadas
        autor (list[Autor]): Lista de autores registrados
    """

    def __init__(self):

        """Inicializa el sistema del museo cargando datos iniciales"""

        self.apidepartamentos = obtener_departamentos() 
        self.departamento = []
        self.iniciar_departamentos()  
        self.obras = []
        self.autor = []

    def start(self):
        
        """Método principal que inicia la interfaz de usuario del sistema
        
        Presenta un menú interactivo con las siguientes opciones:
        1. Ver obras (con submenú de búsqueda)
        2. Mostrar detalles de una obra específica
        3. Salir del sistema
        
        El ciclo continúa hasta que el usuario seleccione la opción de salida
        """

        while True:
            menu = input(""" Buen dia. Bienvenido a MetroArt 
    A continuacion se le muestra un menu de opciones:
    Elija la opcion que desee:
    1- Ver obras
    2- Mostrar detalles de obra
    3- Salir
    ==> """)
            if menu == "1":
                self.opcion_ver_obras()
            elif menu == "2":
                self.mostrar_detalles_obra()
            elif menu == "3":
                break
            else:
                print("Opcion Invalida. Intente de nuevo")
                
    def opcion_ver_obras (self):

        """Muestra submenú para buscar obras por diferentes criterios
        
        Opciones disponibles:
        1. Por departamento
        2. Por nacionalidad del artista
        3. Por nombre de autor
        
        Cada opción llama al método correspondiente para realizar la búsqueda
        """
        
        self.iniciar_departamentos()
        opciones = input("""Seleccione un metodo para buscar una obra:
    1- Ver por Departamento:(Podra ver y escoger el departamento de su preferencia, para posteriormente
                         ver las obras que lo conforman)
    2- Ver por Nacionalidad:(Se le mostraran las obras que correspondan a la nacionalidad seleccionada)
    3- Ver por Autor:(Encontrara todas las obras que correspondan al autor seleccionado)
    ==>    """)
        if opciones == "1":
            for depart in self.departamento:
                    depart.show()
            self.ver_obra_depart()

        elif opciones == "2":
            mostrar_nacionalidades()
            self.buscar_nacionalidad()
        
        elif opciones == "3":
            autores = self.obtener_lista_autores()
            print("Lista de autores encontrados:")
            for autor in autores:
                print(autor)
            self.ver_obras_autor()
                
    def iniciar_departamentos(self):

        """Carga y convierte los datos de departamentos desde la API en objetos Departamentos
        
        Procesa la respuesta de la API para crear instancias de la clase Departamentos
        y las almacena en la lista self.departamento
        """

        departamento_api = self.apidepartamentos["departments"]

        for departamento in departamento_api:
             self.departamento.append(Departamentos(departamento["departmentId"], departamento["displayName"]))
        

    def ver_obra_depart(self):

        """Busca y muestra obras pertenecientes a un departamento específico
        
        El usuario debe ingresar el nombre exacto del departamento
        Muestra hasta 20 obras del departamento seleccionado
        """

        ver_obra = input("Para ver las obras, ingrese el nombre del departamento que desea ver: ")
        dept_id = None
        for d in self.departamento:
            if d.nombre.lower() == ver_obra.lower():
                dept_id = d.id
                break

        if dept_id is None:
            print("Departamento no encontrado")
            return

        import requests
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={dept_id}"
        resp = requests.get(url).json()
        object_ids = resp.get("objectIDs", [])

        if not object_ids:
            print("No se encontraron obras para este departamento")

        for obj_id in object_ids [:20]:
            obra_data = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}").json()

            obra = Obra(obra_data["objectID"], obra_data["title"], obra_data["artistDisplayName"], obra_data["classification"], obra_data["objectDate"], obra_data["primaryImageSmall"])
            obra.show_1()
            print()

    def buscar_nacionalidad(self):

        """Busca obras por nacionalidad del artista
        
        Muestra hasta 10 obras que coincidan con la nacionalidad ingresada
        Maneja errores de conexión y casos donde no se encuentran resultados
        """

        nacionalidad = input("\nIngrese la nacionalidad exacta que desea buscar (ej: American): ").strip() 
        if not nacionalidad:
            print("Debe ingresar una nacionalidad válida")
            return

        try:
            import requests
             
            search_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
            response = requests.get(search_url, timeout=10)
            response.raise_for_status()
            object_ids = response.json().get('objectIDs', [])[:50]

            obras_encontradas = 0

            for obj_id in object_ids:
                try:
                    
                    obra_url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
                    obra_response = requests.get(obra_url, timeout=10)
                    obra_response.raise_for_status()
                    obra_data = obra_response.json()

                    # Verificamos la nacionalidad del artista
                    if obra_data.get('artistNationality', '').lower() == nacionalidad.lower():
                    # Creamos y mostramos la obra
                        obra = Obra(
                        obra_data.get('objectID', ''),
                        obra_data.get('title', 'Sin título'),
                        obra_data.get('artistDisplayName', 'Desconocido'),
                        obra_data.get('classification', ''),
                        obra_data.get('objectDate', ''),
                        obra_data.get('primaryImageSmall', '')
                        )
                    obra.show_1()
                    print() 
                    obras_encontradas += 1

                    # Limitar a 10 resultados para no saturar
                    if obras_encontradas >= 10:
                        break

                except requests.exceptions.RequestException:
                    continue # Si falla una obra, continuamos con la siguiente

            if obras_encontradas == 0:
                print(f"No se encontraron obras para autores de nacionalidad '{nacionalidad}'")
                print("Intente de nuevo")
                
        except requests.exceptions.RequestException as e:
            print(f"\nError al conectar con la API del Museo: {str(e)}")
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {str(e)}")

    def obtener_lista_autores(self, limite=100):

        """Obtiene una lista única de nombres de autores desde la API.
        
        Argumentos:
            limite (int): Número máximo de obras a consultar para extraer autores.
            
        Returns:
            list: Lista ordenada de nombres de autores únicos.
        """

        import requests

        ids_resp = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
        todos_ids = ids_resp.json().get("objectIDs", [])[:limite]

        autores = set()

        for obj_id in todos_ids:
            resp = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
            try:
                obra_data = resp.json()
            except ValueError:
                continue

            nombre_autor = obra_data.get("artistDisplayName", "").strip()
            if nombre_autor:
                autores.add(nombre_autor)

        return sorted(list(autores))

    def ver_obras_autor(self):

        """Busca y muestra obras de un autor específico
        
        Muestra hasta 20 obras que coincidan con el nombre del autor ingresado
        """

        import requests        
        nombre_autor = input("Ingrese el nombre del autor que desea buscar: ").strip().lower()
        ids_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        try:
            resp = requests.get(ids_url, timeout=10)
            resp.raise_for_status()
            object_ids = resp.json().get("objectIDs", [])[:50] 
        except:
            print("Error al obtener la lista de obras")
            return

        if not object_ids:
            print("No se encontraron obras en la base de datos")
            return

        encontrados = 0

        for obj_id in object_ids:
            try:
                r = requests.get(
                    f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}",
                    timeout=10
                )
                if r.status_code != 200:
                    continue  

                obra_data = r.json()
            except:
                continue 

            if obra_data.get("artistDisplayName", "").strip().lower() == nombre_autor:
                obra = Obra(
                    obra_data["objectID"],
                    obra_data["title"],
                    obra_data.get("artistDisplayName", "Desconocido"),
                    obra_data.get("classification", ""),
                    obra_data.get("objectDate", ""),
                    obra_data.get("primaryImageSmall", "")
                )
                obra.show_1()
                print()
                encontrados += 1

                if encontrados >= 20:  # Muestra máximo 20
                    break

        if encontrados == 0:
            print(f"No se encontraron obras del autor '{nombre_autor}'.")

    def mostrar_detalles_obra(self):

        """Muestra información detallada de una obra específica por ID
        
        Incluye opción para visualizar la imagen de la obra si está disponible
        """
    
        import requests
        from PIL import Image
        from io import BytesIO
        
        try:
            obra_id = int(input("Ingrese el ID de la obra: "))
        except ValueError:
            print("El ID debe ser un número")
            return

        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
        resp = requests.get(url)

        if resp.status_code != 200:
            print("No se pudo obtener la obra desde la API")
            return

        data = resp.json()
        if not data or not data.get("objectID"):
            print("No se encontró ninguna obra con ese ID")
            return

        
        autor = Autor(
            nombre=data.get("artistDisplayName", "Desconocido"),
            nacionalidad=data.get("artistNationality", "Desconocida"),
            fecha_nacimiento=data.get("artistBeginDate", "Desconocida"),
            fecha_muerte=data.get("artistEndDate", "Desconocida")
        )

       
        obra = Obra(
            id=data.get("objectID"),
            titulo=data.get("title", "Desconocido"),
            autor=autor.nombre,  
            tipo=data.get("classification", "Desconocido"),
            anio_creacion=data.get("objectDate", "Desconocido"),
            imagen=data.get("primaryImageSmall", None)
        )
        obra.autor_obj = autor  

        # Mostrar detalles
        print()
        obra.show()
        
        # Mostrar imagen si existe
        if obra.imagen:
            ver_img = input("¿Desea ver la imagen? (1=Si / 2=No): ").strip()
            if ver_img == "1":
                try:
                    img_resp = requests.get(obra.imagen)
                    img_resp.raise_for_status()
                    img = Image.open(BytesIO(img_resp.content))
                    img.show()
                except Exception as e:
                    print(f"No se pudo mostrar la imagen: {e}")
        else:
            print("No hay imagen disponible para esta obra")