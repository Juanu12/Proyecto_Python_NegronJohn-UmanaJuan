import json
from Menucoordinador import*
def abrirJSON():
    dicFinal={}
    with open("./Campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Campers.json",'w') as outFile:
        json.dump(dic,outFile)

data={}
data=abrirJSON()
def iniciarSesion(): 

    print("Ingresa tu cedula:")
    ced = input(" : ")

    if ced in data["campers"]:
        print(f"¡Bienvenido", {data[ced]['nombre']}, {data[ced]['apellido']})
        print(f"Tu cedula es:", {data[ced]['cedula']})
        print(f"Tu estado es:", {data[ced]["estado"]})

    else:
        print("Cedula no encontrada. Por favor, verifica tus datos o regístrate.")

    
       
print("Bienvenido a Campuslands")
print("1. Camper")
print("2. Trainer")
print("3. Coordinador")
opc = input(" : ")

if opc == "1":
    print("Bienvenido, Camper")
    print("1. Inicia sesión")
    print("2. Registrarse")
    opce = input(" : ")

    if opce == "1":
        iniciarSesion()
    
    if opce == "2":
        
     print("Ingresa tu numero de documento")
     documento = input(" : ")
     print("Ingresa tu nombre")
     nombre = input(" : ")
     print("Ingresa tu apellido")
     apellido = input(" : ")
     print("Ingresa tu Direccion")
     direccion = input(" : ")
     print("Ingresa el nombre de tu acudiente")
     nombreacudiente = input(" : ")
     print("Ingresa tu numero de Telefono")
     telefono = input(" : ")
     data["campers"][documento]={ "cedula": documento,
                                                 "nombre": nombre,
                                                 "apellido": apellido,
                                                 "Direccion": direccion,
                                                 "Acudiente": nombreacudiente,
                                                 "Telefono": telefono }
    guardarJSON(data)
    print("Estudiante registrado con exito")
        
     
if opc == "2":
    def abrirJSON():
     dicFinal={}
     with open("./Trainer.json",'r') as openFile:
        dicFinal=json.load(openFile)
     return dicFinal

    def guardarJSON(dic):
     with open("./Trainer.json",'w') as outFile:
        json.dump(dic,outFile)

    print("Bienvenido Trainer")
    print("Que quieres hacer como Trainer")
    print("1. Ver tus horarios")
    print("2. Ver tu ruta asignada")
    print("3. Asignar notas")
    print("4. ver salones asignados")
    opct=(input(":"))

    if opct == "1":
     print ("bienvenido a tus horarios")
     trainerho={}
     trainerho = abrirJSON
     print("Docentes",trainerho("Trainers"))
       
    

if opc == "3":
   coordinador()




