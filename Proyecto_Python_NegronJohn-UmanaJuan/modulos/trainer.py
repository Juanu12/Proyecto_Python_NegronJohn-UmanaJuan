import json
from utilss.utilsOs import *

CAMPER_DB = "./db/camper.json"
TRAINERS_DB = "./db/trainer.json"
GRUPOS_DB = "./db/grupos.json"
JORANDA_DB = "./db/jornadas.json"

def calificar():
    campers = cargar_objetos(CAMPER_DB)
    cedula = input('Ingrese cedula del camper :')
    encontrado = False
    for camper in campers:
        if camper.get("cedula") == cedula:
            print("\nExiste un camper con esa cédula. ")
            encontrado = True
            if camper['estado']['Cursando'] == True:
                print('--------Ingresa las notas-----')
                print('....Modulo 1......')
                modulo1Teorica = getInt('Nota Teorica :')
                modulo1Practica = getInt('Nota Practica: ')
                modulo1Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo1 = (modulo1Teorica * 0.3) + (modulo1Practica * 0.6) + (modulo1Quizes * 0.1)
                print('....Modulo 2......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo2Teorica = getInt('Nota Teorica :')
                modulo2Practica = getInt('Nota Practica :')
                modulo2Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo2 = (modulo2Teorica * 0.3) + (modulo2Practica * 0.6) + (modulo2Quizes * 0.1)
                print('....Modulo 3......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo3Teorica = getInt('Nota Teorica :')
                modulo3Practica = getInt('Nota Practica :')
                modulo3Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo3 = (modulo3Teorica * 0.3) + (modulo3Practica * 0.6) + (modulo3Quizes * 0.1)
                print('....Modulo 4......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo4Teorica = getInt('Nota Teorica :')
                modulo4Practica = getInt('Nota Practica :')
                modulo4Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo4 = (modulo4Teorica * 0.3) + (modulo4Practica * 0.6) + (modulo4Quizes * 0.1) 
                print('....Modulo 5......')
                print('Si el camper todavia no ha presentado el siguiente modulo, ingresar (0)')
                modulo5Teorica = getInt('Nota Teorica :')
                modulo5Practica = getInt('Nota Practica :')
                modulo5Quizes = getInt('Ingrese la nota de los trabajos y los quizes :')
                modulo5 = (modulo5Teorica * 0.3) + (modulo5Practica * 0.6) + (modulo5Quizes * 0.1) 

                notas = {
                    "modulo1": modulo1,
                    "modulo2": modulo2,
                    "modulo3": modulo3,
                    "modulo4": modulo4,
                    "modulo5": modulo5
                }

                camper['notas'] = notas

                guardar_objeto(CAMPER_DB, camper)
                break
            else:
                print("")
                print("El Camper no se encuentra cursando.")    
    if not encontrado:
        print('La cedula es incorrecta')

def mostrar_horario_trainer():
    """
    Muestra el horario del trainer.
    
    La función solicita el ID del trainer, carga la base de datos de grupos y jornada,
    filtra los grupos asignados a ese trainer y muestra la información de la jornada asociada.
    
    Se asume que:
      - Cada grupo en "grupos.json" tiene al menos las claves "trainer_id", "grupo" y "jornada_id".
      - Cada jornada en "jornada.json" tiene las claves "id", "hora_inicio", "hora_fin" y "dias".
    """
    clear_terminal()
    print("== Horario del Trainer ==")
    trainer_cc = input("Ingresa tu cedula de Trainer: ")

    # Cargar la información de grupos y jornadas.
    grupos = cargar_objetos(GRUPOS_DB)
    jornadas = cargar_objetos(JORANDA_DB)

    # Filtrar grupos asignados a este trainer.
    grupos_asignados = [grupo for grupo in grupos if grupo.get("trainer") == trainer_cc]

    if not grupos_asignados:
        print(f"\nNo se encontró ningún grupo asignado al Trainer con ID {trainer_cc}.")
        input("\nPresiona Enter para continuar...")
        return

    print(f"\nHorarios asignados para el Trainer con ID {trainer_cc}:\n")
    for grupo in grupos_asignados:
        # Se asume que en cada grupo existe la clave "jornada_id"
        jornada_id = grupo.get("id")
        # Buscar la jornada correspondiente.
        jornada_info = next((j for j in jornadas if j.get("id") == jornada_id), None)
        if jornada_info:
            print(f"  Hora: {jornada_info.get('horario')}")
            print("-" * 40)
        else:
            print(f"\nNo se encontró información de la jornada (ID: {jornada_id}) para el grupo {grupo.get('grupo', 'N/A')}.")
    input("\nPresiona Enter para continuar...")
