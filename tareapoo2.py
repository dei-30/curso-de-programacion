import time

class Estudiante:
    def __init__(self, nombre, nivel, mana, hechizos_aprendidos):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.hechizos_aprendidos = hechizos_aprendidos

    def aprender_hechizo(self, hechizo):
        self.hechizos_aprendidos.append(hechizo)
        print(f"Hechizo {hechizo} aprendido por {self.nombre}")

    def lanzar_hechizo(self, hechizo, objetivo):
        if hechizo in self.hechizos_aprendidos:
            print(f"{self.nombre} lanza {hechizo} a {objetivo.nombre}")
        else:
            print(f"{self.nombre} no conoce el hechizo {hechizo}")

    def recargar_mana(self, cantidad):
        self.mana += cantidad
        print(f"{self.nombre} ha recargado {cantidad} de mana. Mana actual: {self.mana}")

    def mostrar_estado(self):
        print(f"Estudiante: {self.nombre}, Nivel: {self.nivel}, Mana: {self.mana}, Hechizos: {', '.join(self.hechizos_aprendidos)}")


class Profesor:
    def __init__(self, nombre, especialidad,mana, experiencia, hechizos_domina):
        self.nombre = nombre
        self.especialidad = especialidad
        self.mana = mana
        self.experiencia = experiencia
        self.hechizos_domina = hechizos_domina

    def enseñar_hechizo(self, estudiante, hechizo):
        estudiante.aprender_hechizo(hechizo)
        print(f"{self.nombre} ha enseñado {hechizo} a {estudiante.nombre}")

    def evaluar(self, estudiante):
        print(f"{self.nombre} está evaluando a {estudiante.nombre}")
        if estudiante.nivel < 5:
            estudiante.nivel += 1
            print(f"{estudiante.nombre} ha subido a nivel {estudiante.nivel}")
        else:
            print(f"{estudiante.nombre} ya está en el nivel máximo")

    def mostrar_estado(self):
        print(f"Profesor: {self.nombre}, Especialidad: {self.especialidad}, Mana: {self.mana}, Experiencia: {self.experiencia} años")


class Hechizo:
    def __init__(self, nombre, daño, costo_mana, tipo):
        self.nombre = nombre
        self.daño = daño
        self.costo_mana = costo_mana
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Hechizo: {self.nombre}, Daño: {self.daño}, Costo de Mana: {self.costo_mana}, Tipo: {self.tipo}")


class Duelista:
    def __init__(self, estudiante, profesor):
        self.estudiante = estudiante
        self.profesor = profesor

    def iniciar_duelo(self):
        print(f"El duelo entre {self.estudiante.nombre} y {self.profesor.nombre} ha comenzado!")
        turno = 100
        while self.estudiante.mana > 100 and self.profesor.mana > 100 and turno < 10:
            atacante = self.estudiante if turno % 2 == 0 else self.profesor
            defensor = self.profesor if turno % 2 == 0 else self.estudiante

            if atacante.hechizos_aprendidos:
                hechizo = atacante.hechizos_aprendidos[0]
                print(f"{atacante.nombre} lanza {hechizo} a {defensor.nombre}")
                atacante.mana -= 10
            else:
                print(f"{atacante.nombre} no tiene hechizos para lanzar!")

            turno += 1

        ganador = self.estudiante if self.estudiante.mana > 0 else self.profesor
        print(f"El duelo ha terminado! El ganador es {ganador.nombre}")


class Academia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_estudiantes = ["darwin"]
        self.lista_profesores = []

    def matricular_estudiante(self, estudiante):
        self.lista_estudiantes.append(estudiante)
        print(f"Estudiante {estudiante.nombre} agregado a la academia {self.nombre}")

    def asignar_profesor(self, profesor):
        self.lista_profesores.append(profesor)
        print(f"Profesor {profesor.nombre} agregado a la academia {self.nombre}")

    def organizar_duelo(self, estudiante_nombre, profesor_nombre):
        estudiante = next((e for e in self.lista_estudiantes if e.nombre == estudiante_nombre), None)
        profesor = next((p for p in self.lista_profesores if p.nombre == profesor_nombre), None)

        if estudiante and profesor:
            duelo = Duelista(estudiante, profesor)
            duelo.iniciar_duelo()
        else:
            print("Estudiante o profesor no encontrado en la academia")

    def mostrar_academia(self):
        print(f"Academia: {self.nombre}")
        print("Estudiantes:")
        for estudiante in self.lista_estudiantes:
            estudiante.mostrar_estado()
        print("Profesores:")
        for profesor in self.lista_profesores:
            profesor.mostrar_estado()

time.sleep(1)
mi_academia = Academia("Hogwarts")
estudiante1 = Estudiante("Harry", 4, 100, ["Expelliarmus"])
profesor1 = Profesor("Dumbledore", "Defensa Contra las Artes Oscuras",100, 50, ["Expecto Patronum"])
mi_duelo = Duelista(estudiante1, profesor1)

# Matricular estudiante y asignar profesor
mi_academia.matricular_estudiante(estudiante1)
mi_academia.asignar_profesor(profesor1)

# Mostrar estado de la academia
mi_academia.mostrar_academia()

# Organizar duelo
mi_academia.organizar_duelo("Harry", "Dumbledore")

