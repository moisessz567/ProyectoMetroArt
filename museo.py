from departamentos import Departamentos
from obra import Obra
from autor import Autor
from API import obtener_departamentos, obtener_obras


class Museo:
    def __init__(self):
        self.apidepartamentos = obtener_departamentos()  # Llama directamente a la función
        self.departamento = []
        self.iniciar_departamentos()  # Inicializa los departamentos al crear el objeto
        self.apiobras = obtener_obras()
        self.obras = []
        self.autor = []

    def start(self):
        
        
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
        self.iniciar_departamentos()
        self.iniciar_autor()
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
            pass
        
        elif opciones == "3":
            for autor in self.autor:
                autor.show()
            self.ver_obras_autor()
                
    def iniciar_departamentos(self):
        departamento_api = self.apidepartamentos["departments"]

        for departamento in departamento_api:
             self.departamento.append(Departamentos(departamento["departmentId"], departamento["displayName"]))
        

    def ver_obra_depart(self):

        # Preguntar el nombre del departamento
        ver_obra = input("Para ver las obras, ingrese el nombre del departamento que desea ver: ")

        # Buscar ID del departamento
        dept_id = None
        for d in self.departamento:
            if d.nombre.lower() == ver_obra.lower():
                dept_id = d.id
                break

        if dept_id is None:
            print("Departamento no encontrado")
            return

        # Llamar a la API para obtener IDs de obras de ese departamento
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


    def iniciar_obras(self):
        obras_api = self.apiobras["objects"]
        for obra in obras_api:
            self.obras.append(Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["classification"], obra["objectDate"], obra["primaryImage"]))

    def iniciar_autor(self):
        pass
        # autor_api = self.apiobras["objects"]
        # for autor in autor_api:
        #     self.autor.append(Autor(autor["artistDisplayName"], autor["artistNationality"], autor["artistBeginDate"], autor["artistEndDate"]))

    def ver_obras_autor(self):
        import requests
        # Suponiendo que self.obras es una lista de objetos de la clase Obra
        buscar_autor = input("Ingrese el nombre y apellido del autor: ")
        # Inicializar una lista para almacenar las obras encontradas
        obras_encontradas = []
        # Buscar el autor en la lista de obras
        for a in self.obras:
            if a.nombre.lower() == buscar_autor.lower():
                obras_encontradas.append(a)  # Agregar la obra a la lista si el autor coincide
        # Verificar si se encontraron obras del autor
        if not obras_encontradas:
            print("Autor no encontrado")
        else:
            print(f"Obras encontradas para el autor '{buscar_autor}':")
    
        # Obtener las obras de la API
        response = requests.get("https://collectionapi.metmuseum.org/public/collection/v1/objects")
        object_ids = response.json().get("objectIDs", [])  # Obtener los primeros 100 IDs de objetos

        if not object_ids:
            print("No se encontraron obras para este autor")
        else:
            for obj_id in object_ids:
                obj_url = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}")
                obj_data = obj_url.json()
            # Verificar si el autor de la obra coincide con el autor buscado
            if obj_data.get("artistDisplayName").lower() == buscar_autor.lower():
                obra = Obra(
                    obj_data["objectID"],
                    obj_data["title"],
                    obj_data["artistDisplayName"],
                    obj_data["classification"],
                    obj_data["objectDate"],
                    obj_data["primaryImageSmall"]
                )
                obra.show_1()  # Mostrar la obra
                print()  # Espacio entre obras

    def mostrar_detalles_obra(self):
    
        import requests
        from PIL import Image
        from io import BytesIO
        
        try:
            obra_id = int(input("Ingrese el ID de la obra: "))
        except ValueError:
            print("El ID debe ser un número.")
            return

        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obra_id}"
        resp = requests.get(url)

        if resp.status_code != 200:
            print("No se pudo obtener la obra desde la API.")
            return

        data = resp.json()
        if not data or not data.get("objectID"):
            print("No se encontró ninguna obra con ese ID.")
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
            print("No hay imagen disponible para esta obra.")