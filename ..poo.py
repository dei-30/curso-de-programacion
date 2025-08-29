class hola_profe:
    def __init__(self):
        self.nombre = "Daniel Z"
        self.apellido = "Espitia"
        self.materia = "Programación"
    
    def saludar(self):
        print(f"Hola chicos, mi nombre es: {self.nombre} {self.apellido}. Y les quiero dar la bienvenida a la clase de {self.materia}.")

    def es_profesor(self, es_profesor=True):
        if es_profesor:
            print(f"Eres el profesor? True")
        else:
            print(f"Eres el profesor? False")


hola = hola_profe()
hola.saludar()
hola.es_profesor(True)
