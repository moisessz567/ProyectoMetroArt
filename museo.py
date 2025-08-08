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
                pass
            elif menu == "3":
                break
            else:
                print("Opcion Invalida. Intente de nuevo")
                
    def opcion_ver_obras (self):
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
            pass
            
                
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
            print("Departamento no encontrado.")
            return

        # Llamar a la API para obtener IDs de obras de ese departamento
        import requests
        url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects?departmentIds={dept_id}"
        resp = requests.get(url).json()
        object_ids = resp.get("objectIDs", [])

        if not object_ids:
            print("No se encontraron obras para este departamento.")
            return

        # Mostrar TODAS las obras con dos saltos de línea entre cada una
        for obj_id in object_ids [:20]:
            obra_data = requests.get(
                f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{obj_id}"
            ).json()

            obra = Obra(
                obra_data["objectID"], obra_data["title"], obra_data["artistDisplayName"], obra_data["classification"], obra_data["objectDate"], obra_data["primaryImageSmall"])
            obra.show_1()
            print()


    def iniciar_obras(self):
        obras_api = self.apiobras["objects"]
        for obra in obras_api:
            self.obras.append(Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["classification"], obra["objectDate"], obra["primaryImage"]))

    def ver_obras_autor(self):
        self.iniciar_obras()
        autor_api = self.apiobras["Objects"]["artistDisplayName"]
        self.autor = []

        for artist in autor_api:
            self.autor.append(Autor(artist["artistDisplayName"], artist["artistNationality"], artist["artistBeginDate"], artist["artistEndDate"]))

        