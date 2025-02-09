class Horario:
    def __init__(self):
        
        self.dias = {
            "Lunes": [],
            "Martes": [],
            "Miércoles": [],
            "Jueves": [],
            "Viernes": []
        }
        
    def agregar_clase(self, dia, hora, ruta, salon, profesor):
        if dia in self.dias:
            clase = {"hora": hora, "ruta": ruta, "salon": salon, "profesor": profesor}
            self.dias[dia].append(clase)
            print(f"Clase de {ruta} en el salón {salon} agregada para {dia} a las {hora} con {profesor}.")
    
    def mostrar_horario(self):
        print("Horario semanal:")
        for dia, clases in self.dias.items():
            print(f"\n{dia}:")
            for clase in clases:
                print(f"  {clase['hora']} - {clase['materia']} (Salón: {clase['salon']}, Profesor: {clase['profesor']})")
            
salones = {
    "Java": "Salón 1" [],
    "NodeJS": "Salón 2"[],
    ".NET Core": "Salón 3"[]
}

profesores = {
    "Java": "Profesor Juan",
    "NodeJS": "Profesora María",
    ".NET Core": "Profesor Carlos"
}

mi_horario = Horario()
horas = ["06:00 AM", "10:00 AM", "02:00 PM", "06:00 PM",]

mi_horario.agregar_clase("Lunes","Hora de inicio", horas[0], "Java", salones["Java"], profesores["Java"])
mi_horario.agregar_clase("Lunes","Hora de inicio", horas[1], "NodeJS", salones["NodeJS"], profesores["NodeJS"])
mi_horario.agregar_clase("Lunes","Hora de inicio", horas[2], ".NET Core", salones[".NET Core"], profesores[".NET Core"])
mi_horario.agregar_clase("Lunes","Hora de inicio", horas[3], "Java", salones["Java"], profesores["Java"])

mi_horario.agregar_clase("Martes","Hora de inicio", horas[0], "NodeJS", salones["NodeJS"], profesores["NodeJS"])
mi_horario.agregar_clase("Martes","Hora de inicio", horas[1], ".NET Core", salones[".NET Core"], profesores[".NET Core"])
mi_horario.agregar_clase("Martes","Hora de inicio", horas[2], "Java", salones["Java"], profesores["Java"])
mi_horario.agregar_clase("Martes","Hora de inicio", horas[3], "NodeJS", salones["NodeJS"], profesores["NodeJS"])


mi_horario.agregar_clase("Miércoles","Hora de inicio", horas[0], ".NET Core", salones[".NET Core"], profesores[".NET Core"])
mi_horario.agregar_clase("Miércoles","Hora de inicio", horas[1], "Java", salones["Java"], profesores["Java"])
mi_horario.agregar_clase("Miércoles","Hora de inicio", horas[2], "NodeJS", salones["NodeJS"], profesores["NodeJS"])
mi_horario.agregar_clase("Miércoles","Hora de inicio", horas[3], ".NET Core", salones[".NET Core"], profesores[".NET Core"])


mi_horario.agregar_clase("Jueves","Hora de inicio", horas[0], "Java", salones["Java"], profesores["Java"])
mi_horario.agregar_clase("Jueves","Hora de inicio", horas[1], "NodeJS", salones["NodeJS"], profesores["NodeJS"])
mi_horario.agregar_clase("Jueves","Hora de inicio", horas[2], ".NET Core", salones[".NET Core"], profesores[".NET Core"])
mi_horario.agregar_clase("Jueves","Hora de inicio", horas[3], "Java", salones["Java"], profesores["Java"])


mi_horario.agregar_clase("Viernes","Hora de inicio", horas[0], "NodeJS", salones["NodeJS"], profesores["NodeJS"])
mi_horario.agregar_clase("Viernes","Hora de inicio", horas[1], ".NET Core", salones[".NET Core"], profesores[".NET Core"])
mi_horario.agregar_clase("Viernes","Hora de inicio", horas[2], "Java", salones["Java"], profesores["Java"])
mi_horario.agregar_clase("Viernes","Hora de inicio", horas[3], "NodeJS", salones["NodeJS"], profesores["NodeJS"])


mi_horario.mostrar_horario()