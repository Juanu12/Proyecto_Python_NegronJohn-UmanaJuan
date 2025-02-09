import json
def abrirJSON():
    dicFinal={}
    with open("./Campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Campers.json",'w') as outFile:
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

if opct == "2":
  print ("bienvenido a tu ruta")
  trainerho={}
  trainerho = abrirJSON
  print("Docentes",trainerho("Trainers"))

if opct == "3":
  print("A que estudiante quieres asignarles notas")
  def abrirJSON():
    dicFinal={}
    with open("./Campers.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./Campers.json",'w') as outFile:
        json.dump(dic,outFile)

estudiantenotas = {}
estudiantenotas = abrirJSON
agregarnotas= {}
agregarnotas = abrirJSON
print("Ingresa la cedula/tarjeta de identidad del estudiante a asignar nota de examen de ingreso:")
iden = input(" : ")
notasag = input(" Ingresa la nota que saco en el examen de ingreso ")

if iden in estudiantenotas["campers"]:
   notasag == 60 or notasag > 60
   notasag= True
   print(f"Camper",{estudiantenotas["campers"]["nombre"]})
   agregarnotas.append[notasag["campers"]["notaexamen"]]
   nuevanota= {
       "notaexamen": notasag
     }
   
else: notasag == 60 or notasag > 60 
agregarnotas.append[notasag["campers"]["notaexamen"]]
agregarnotas.append[notasag["campers"]["estado"]:["aprobado"]]



if notasag < 60 :   
 print("estudiante no aprobado")
agregarnotas.append[notasag["campers"]["estado"]:["desaprobado"]]
    

estudiantenotas({["campers"]["notaexamen"]}).append(nuevanota)
guardarJSON(estudiantenotas)
print("Estudiante añadida con exito")




