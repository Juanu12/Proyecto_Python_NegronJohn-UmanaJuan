import json

def abrirJSON():
    dicFinal={}
    with open("./Campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
def guardarJSON(dic):
    with open("./Campers.json",'w') as outFile:
        json.dump(dic,outFile)
     
     
data ={}     
data = abrirJSON()
 
def coordinador():




 print("Bienvenido coordinador")
 print("Que deseas hacer como cordinador? ")
 print("1. Agregar estudiante")
 print("2. Ver estudiantes")
 print("3. Editar estudiantes")
 print("4. Asignar estudiante a curso ")
 print("5. Eliminar estudiantes")
 print("6. Agregar nuevas rutas de estudio")
opcc = input(" : ")

if opcc == "1":
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

if opcc == "2":
    verest={}
    verest = abrirJSON
    for i in range (len(verest["campers"](nombre))):
    
     print("Estudiante#",i+1, { verest[nombre]} +i )
  



  