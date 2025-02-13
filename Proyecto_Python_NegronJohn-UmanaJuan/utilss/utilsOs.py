import os
import json

def getInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except Exception:
            print('Opcion Invalida, ingrese un valor valido.')

def cargar_objetos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            if isinstance(datos, list):
                return datos
            else:
                print("Error: El contenido del archivo no es un array. Se retorna una lista vacía.")
                return []
    except FileNotFoundError:
        print("Error: El archivo no existe. Se retorna una lista vacía.")
        return []
    except json.JSONDecodeError:
        print("Error: El archivo no contiene un JSON válido. Se retorna una lista vacía.")
        return []

def guardar_objeto(nombre_archivo, objeto):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
            if not isinstance(datos, list):
                print("Advertencia: El contenido del archivo no es un array. Se creará uno nuevo.")
                datos = []
    except FileNotFoundError:
        print("Advertencia: El archivo no existe. Se creará uno nuevo.")
        datos = []
    except json.JSONDecodeError:
        print("Advertencia: El archivo no contiene un JSON válido. Se creará uno nuevo.")
        datos = []

    # Añadir el nuevo objeto al array
    datos.append(objeto)
    
    # Guardar el array actualizado en el archivo
    with open(nombre_archivo, 'w') as archivo:
        json.dump(datos, archivo, indent=4)
    print("Objeto guardado exitosamente.")


def validar_opcion(opcion, min_op, max_op):
    try:
        num = int(opcion)
    except ValueError:
        return None 

    if min_op <= num <= max_op:
        return num
    else:
        return None

def obtener_opcion_valida(mensaje, min_op, max_op):
    while True:
        opcion = input(mensaje)
        opcion_validada = validar_opcion(opcion, min_op, max_op)
        if opcion_validada is not None:
            return opcion_validada
        else:
            print(f"Opción inválida. Ingresa un número entre {min_op} y {max_op}.")

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
