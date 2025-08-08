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
    2- Ver horarios
    ==> """)
            if menu == "1":
                self.opcion_ver_obras()
            elif menu == "2":
                print("""Los Horarios de consulta son: 
                      
Lunes: 6 am - 11 pm
Martes: 6 am - 11 pm
Miercoles: 6 am - 11 pm
Jueves: 6 am - 11 pm
Viernes: 6 am - 10 pm
Sabado: 8 am - 10 pm
Domingo: 8 am - 9 pm 
                      """)
                
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
                    print()
                    depart.show()
            self.ver_obra_depart()

        elif opciones == "2":
            pass
            
            
                
    def iniciar_departamentos(self):
        departamento_api = self.apidepartamentos["departments"]

        for departamento in departamento_api:
             self.departamento.append(Departamentos(departamento["departmentId"], departamento["displayName"]))
        

    def ver_obra_depart(self):
        departamento_nombre = None
        ver_obra = input("Para ver las obras, ingrese el nombre del departamento que desea ver: ")
        for obra_dep in self.apiobras:
            if obra_dep["departments"] == ver_obra:
                departamento_nombre = obra_dep["departments"]
        for obra in self.obras:
            if departamento_nombre == obra_dep["departments"]:
                obras = (Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["classification"], obra["objectDate"], obra["primaryImage"]))
                obras.show()


    def iniciar_obras(self):
        obras_api = self.apiobras["objects"]
        for obra in obras_api:
            self.obras.append(Obra(obra["objectID"], obra["title"], obra["artistDisplayName"], obra["classification"], obra["objectDate"], obra["primaryImage"]))
