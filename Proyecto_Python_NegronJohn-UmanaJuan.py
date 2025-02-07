import json

def abrirJSON():
    dicFinal={}
    with open("./campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./campers.json",'w') as outFile:
        json.dump(dic,outFile)

print("Bievenido a Campuslands")
print("1. Camper")
print("2.Trainer ")
print("3.COORDINADOR")
opce = input(":")

if opce == "1":
 print("Bienvenido, Camper")
 print("Bievenido a Campuslands")
print("1. Inicia sesion")
print("2. Registrarse")
opc = (input(" : "))



if opc == "2":
    doc=(input("Ingresa tu numero de documento"))
    print(" : ")
    nom=(input("Ingresa tu nombre"))
    print(" : ")
    app=(input("Ingresa tu apellido"))
    print(" : ")
    direc=(input("Ingresa tu Direccion"))
    print(" : ")
    nomac=(input("Ingresa el nombre de tu acudiente"))
    print(" : ")
    numtel=int=(input("Ingresa tu numero de Telefono"))
    print(" : ")

registroestudiante={}
nuevoestudiante= {
    "cedula": "doc",
    "nombre": "nom",
    "apellido": "app",
    "Dirección": "direc",
    "Acudiente": "nomac",
    "Telefono": "numtel"
    }
nuevoestudiante.update(nuevoestudiante)
guardarJSON(nuevoestudiante)
print("Estudiante añadido con exito")



if opce =="2":
 print("Bienvenido Trainer")

 if opce == "3":
  print("Bienvenido COORDINADOR")







