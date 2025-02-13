#!/usr/bin/env python3
import json
from utilss.utilsOs import *  # Se asume que este módulo importa: clear_terminal, obtener_opcion_valida, cargar_objetos, guardar_objeto

NOMBRE_ARCHIVO = "./db/camper.json"

def registrarse():
    """Caso de uso: Registrarse."""
    clear_terminal()
    print("== Registro de Camper ==")
    cedula = input("Ingresa tu cédula: ")

    # Cargar campers existentes para validar la unicidad de la cédula
    campers = cargar_objetos(NOMBRE_ARCHIVO)
    for camper in campers:
        if camper.get("cedula") == cedula:
            print("\nError: Ya existe un camper con esa cédula. Intenta con otro ID.")
            input("\nPresiona Enter para continuar...")
            return  # Sale de la función sin registrar el nuevo camper

    # Si la cédula es única, se continúa con el registro
    nombre    = input("Ingresa tu nombre: ")
    apellido  = input("Ingresa tu apellido: ")
    direccion = input("Ingresa tu dirección: ")
    acudiente = input("Ingresa el nombre de tu acudiente: ")
    telefono  = input("Ingresa tu teléfono: ")
    telefonoFijo = input("Ingresa tu teléfono fijo (opcional): ")
    
    # Se crean los campos adicionales según la DB con valores por defecto.
    nuevo_camper = {
        "cedula": cedula,
        "nombre": nombre,
        "apellido": apellido,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono": telefono,
        "telefonoFijo": telefonoFijo,
        "estado": {
            "En proceso": True,
            "Inscrito": False,
            "Aprobado": False,
            "Denegado": False,
            "Cursando": False,
            "Graduado": False,
            "Expulsado": False,
            "Retirado": False
        },
        "notas": {
            "modulo1": 0.0,
            "modulo2": 0.0,
            "modulo3": 0.0,
            "modulo4": 0.0,
            "modulo5": 0.0
        },
        "riesgo": False,
        "grupo": ""
    }
    
    # Se usa la función de utils para agregar el objeto al array.
    guardar_objeto(NOMBRE_ARCHIVO, nuevo_camper)
    input("\n¡Registrado exitosamente! Presiona Enter para continuar...")


def ingresar():
    """Caso de uso: Ingresar (Iniciar sesión)."""
    clear_terminal()
    print("== Ingreso de Camper ==")
    cedula = input("Ingresa tu cédula: ")
    
    campers = cargar_objetos(NOMBRE_ARCHIVO)
    encontrado = False
    for camper in campers:
        if camper.get("cedula") == cedula:
            print("\n¡Bienvenido(a)! Estos son tus datos:")
            for clave, valor in camper.items():
                if isinstance(valor, dict):
                    print(f"  {clave}:")
                    for subclave, subvalor in valor.items():
                        print(f"      {subclave}: {subvalor}")
                else:
                    print(f"  {clave}: {valor}")
            encontrado = True
            break
    if not encontrado:
        print("\nNo se encontró un camper con esa cédula.")
    input("\nPresiona Enter para continuar...")

def retirarse():
    """Caso de uso: Retirarse de CampusLands."""
    clear_terminal()
    print("== Retiro de CampusLands ==")
    cedula = input("Ingresa tu cédula para retirar tu registro: ")
    
    campers = cargar_objetos(NOMBRE_ARCHIVO)
    indice = None
    for i, camper in enumerate(campers):
        if camper.get("cedula") == cedula:
            indice = i
            print("\nSe encontró tu registro:")
            for clave, valor in camper.items():
                if isinstance(valor, dict):
                    print(f"  {clave}:")
                    for subclave, subvalor in valor.items():
                        print(f"      {subclave}: {subvalor}")
                else:
                    print(f"  {clave}: {valor}")
            break

    if indice is None:
        print("\nNo se encontró un camper con esa cédula.")
    else:
        confirm = input("\n¿Seguro que deseas retirarte? (s/n): ")
        if confirm.lower() == 's':
            # Actualizamos el estado del usuario: marcamos "Retirado" como True.
            campers[indice]["estado"]["Retirado"] = True
            # Opcionalmente, se puede actualizar otros campos, por ejemplo:
            # campers[indice]["estado"]["Inscrito"] = False
            with open(NOMBRE_ARCHIVO, 'w') as archivo:
                json.dump(campers, archivo, indent=4)
            print("\nTu estado se ha actualizado a 'Retirado' en CampusLands.")
        else:
            print("\nOperación cancelada.")
    input("\nPresiona Enter para continuar...")
