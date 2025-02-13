from utilss.utilsOs import *

def menu1():
    menu = (
        "┌───────────────────────────────┐\n"
        "│   Bienvenidos a CampusLands   │\n"
        "└───────────────────────────────┘\n"
        "┌───────────────────────────────┐\n"
        "│           Ingresa:            │\n"
        "├───────────────────────────────┤\n"
        "│ 1. Camper                     │\n"
        "│ 2. Trainer                    │\n"
        "│ 3. Coordinador                │\n"
        "│ 4. Cerrar Sesion              │\n"
        "└───────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 4)


# 1. Camper
def menuEntrarCamper1():
    menu = (
        "┌────────────────────────────────────────┐\n"
        "│               Ingresa:                 │\n"
        "├────────────────────────────────────────┤\n"
        "│ 1. Registrarse                         │\n"
        "│ 2. Ingresar                            │\n"
        "│ 3. Retirarse de CampusLands            │\n"
        "└────────────────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 4)

# 2. Trainer
def menuTrainer():
    menu = (
        "┌───────────────────────────────┐\n"
        "│         Trainer Menu          │\n"
        "├───────────────────────────────┤\n"
        "│ 1. Calificar                  │\n"
        "│ 2. Ver Horario                │\n"
        "└───────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 3)


# 3. Coordinador
def menuCoordinador():
    menu = (
        "┌────────────────────────────────────────────┐\n"
        "│              Coordinador                   │\n"
        "├────────────────────────────────────────────┤\n"
        "│ 1. Administrador Campers                   │\n"
        "│ 2. Administrador Grupos                    │\n"
        "│ 3. Notas Camper                            │\n"
        "└────────────────────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 6)


# 3.1 Coordinador - Campers
def menuCamperCoordinador():
    menu = (
        "┌───────────────────────────────┐\n"
        "│     Coordinador - Campers     │\n"
        "├───────────────────────────────┤\n"
        "│ 1. Crear Camper               │\n"
        "│ 2. Leer Camper                │\n"
        "│ 3. Retirar Camper             │\n"
        "└───────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 3)

def menuAdministrarGrupos():
    menu = (
        "┌────────────────────────────────────────────┐\n"
        "│         Administrar Grupos                 │\n"
        "├────────────────────────────────────────────┤\n"
        "│ 1. Ver Grupos disponibles                  │\n"
        "│ 2. Agregar Grupo                           │\n"
        "│ 3. Editar Grupo                            │\n"
        "└────────────────────────────────────────────┘\n"
        "Selecciona una opción: "
    )
    return obtener_opcion_valida(menu, 1, 4)
