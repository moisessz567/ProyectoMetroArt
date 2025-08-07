from departamentos import Departamentos
from obra import Obra
from autor import Autor
from API import pull_departamentos

class Museo:
    def __init__(self, api):
        self.api = api
    def start(self):
        
        
        while True:
            menu = input(""" Buen dia. Bienvenido a MetroArt 
    A continuacion se le muestra un menu de opciones:
    Elija la opcion que desee:
    1- Ver obras
    2- Ver horarios
    3- Ver recorridos disponibles
    ==> """)
            if menu == "1":
                print()
                self.opcion_ver_obras()
                
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
                
    def iniciar_departamentos(self):
         departamento_api = self.api["departments"]
         self.departamento = []

         for departamento in departamento_api:
             self.departamento.append(Departamentos(departamento["departmentId"], departamento["displayName"]))

    def iniciar_obras(self):
        obras_api = self.api("departments")
        self.obras = []

        for autor in obras_api:
            self.departamento.append(Autor(autor["departmentId"], autor["displayName"]))
