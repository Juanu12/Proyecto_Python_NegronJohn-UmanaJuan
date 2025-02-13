#!/usr/bin/env python3
import json

FILENAME = "./db/grupos.json"

def cargar_grupos():
    """
    Carga la lista de grupos desde el archivo JSON.
    Si el archivo no existe o el contenido es inválido, retorna una lista vacía.
    """
    try:
        with open(FILENAME, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                print("Error: El contenido del archivo no es un array. Se retorna una lista vacía.")
                return []
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: El archivo no contiene un JSON válido. Se retorna una lista vacía.")
        return []

def guardar_grupos(grupos):
    """
    Guarda la lista de grupos en el archivo JSON.
    """
    with open(FILENAME, 'w') as f:
        json.dump(grupos, f, indent=4)

def crear_grupo():
    """
    Solicita los datos para crear un nuevo grupo y lo agrega a la base de datos.
    El id se asigna automáticamente como (máximo id existente + 1).
    """
    grupos = cargar_grupos()
    next_id = 1
    if grupos:
        next_id = max(grupo["id"] for grupo in grupos) + 1
    
    nombre = input("Ingresa el nombre del grupo: ")
    trainer = input("Ingresa el trainer: ")
    jornada = input("Ingresa la jornada: ")
    ruta = input("Ingresa la ruta: ")
    salon = input("Ingresa el salón: ")
    try:
        cantidad = int(input("Ingresa la cantidad: "))
    except ValueError:
        print("Cantidad inválida. Se asigna 0 por defecto.")
        cantidad = 0
    graduado_input = input("¿Graduado? (s/n): ")
    graduado = True if graduado_input.lower() == 's' else False

    nuevo_grupo = {
        "id": next_id,
        "nombre": nombre,
        "trainer": trainer,
        "jornada": jornada,
        "ruta": ruta,
        "salon": salon,
        "cantidad": cantidad,
        "graduado": graduado
    }
    
    grupos.append(nuevo_grupo)
    guardar_grupos(grupos)
    print("\nGrupo creado exitosamente.")

def listar_grupos():
    """
    Muestra en pantalla todos los grupos almacenados en la base de datos.
    """
    grupos = cargar_grupos()
    if not grupos:
        print("No hay grupos registrados.")
        return
    print("== Listado de Grupos ==")
    for grupo in grupos:
        print(f"ID: {grupo['id']}")
        print(f"Nombre: {grupo['nombre']}")
        print(f"Trainer: {grupo['trainer']}")
        print(f"Jornada: {grupo['jornada']}")
        print(f"Ruta: {grupo['ruta']}")
        print(f"Salón: {grupo['salon']}")
        print(f"Cantidad: {grupo['cantidad']}")
        print(f"Graduado: {grupo['graduado']}")
        print("-" * 30)

def actualizar_grupo():
    """
    Permite actualizar los datos de un grupo existente.
    Se busca el grupo por su id y se solicita el nuevo valor para cada campo.
    Si se deja el campo en blanco, se conserva el valor anterior.
    """
    grupos = cargar_grupos()
    try:
        id_buscar = int(input("Ingresa el id del grupo a actualizar: "))
    except ValueError:
        print("ID inválido.")
        return

    grupo_encontrado = None
    for grupo in grupos:
        if grupo["id"] == id_buscar:
            grupo_encontrado = grupo
            break

    if not grupo_encontrado:
        print("Grupo no encontrado.")
        return

    print("Deja en blanco para mantener el valor actual.")
    nombre = input(f"Nombre ({grupo_encontrado['nombre']}): ") or grupo_encontrado["nombre"]
    trainer = input(f"Trainer ({grupo_encontrado['trainer']}): ") or grupo_encontrado["trainer"]
    jornada = input(f"Jornada ({grupo_encontrado['jornada']}): ") or grupo_encontrado["jornada"]
    ruta = input(f"Ruta ({grupo_encontrado['ruta']}): ") or grupo_encontrado["ruta"]
    salon = input(f"Salón ({grupo_encontrado['salon']}): ") or grupo_encontrado["salon"]
    
    cantidad_input = input(f"Cantidad ({grupo_encontrado['cantidad']}): ")
    try:
        cantidad = int(cantidad_input) if cantidad_input.strip() != "" else grupo_encontrado["cantidad"]
    except ValueError:
        print("Cantidad inválida. Se mantiene el valor actual.")
        cantidad = grupo_encontrado["cantidad"]

    graduado_input = input(f"Graduado ({'s' if grupo_encontrado['graduado'] else 'n'}): ")
    if graduado_input.strip() == "":
        graduado = grupo_encontrado["graduado"]
    else:
        graduado = True if graduado_input.lower() == 's' else False

    # Actualizamos los campos
    grupo_encontrado["nombre"] = nombre
    grupo_encontrado["trainer"] = trainer
    grupo_encontrado["jornada"] = jornada
    grupo_encontrado["ruta"] = ruta
    grupo_encontrado["salon"] = salon
    grupo_encontrado["cantidad"] = cantidad
    grupo_encontrado["graduado"] = graduado

    guardar_grupos(grupos)
    print("Grupo actualizado exitosamente.")