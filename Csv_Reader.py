import csv
import os

def leer_csv():
    """
    Lee datos.csv y devuelve una lista con las nacionalidades (no usa variables globales).
    """
    ruta_csv = os.path.join(os.path.dirname(__file__), "datos.csv")
    nacionalidades = []
    try:
        with open(ruta_csv, mode="r", encoding="utf-8") as file:
            lector_csv = csv.reader(file)
            next(lector_csv, None)  # saltar cabecera si existe
            for fila in lector_csv:
                if fila and fila[0].strip():
                    nacionalidades.append(fila[0].strip())
    except FileNotFoundError:
        print(f"No se encontró el archivo: {ruta_csv}")
    return nacionalidades

def mostrar_nacionalidades():
    """
    Muestra la lista numerada de nacionalidades y devuelve la lista leída.
    """
    nacionalidades = leer_csv()
    if not nacionalidades:
        print("No hay nacionalidades disponibles.")
        return nacionalidades

    for i, n in enumerate(nacionalidades, start=1):
        print(f"{i:3d}. {n}")
    return nacionalidades