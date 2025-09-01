class Alumno:
    def __init__ (self, saludar, hacer_examen, salir_del_salon, responder_el_examen ,entregar_tarea, recibir_las_notas ):
        self.saludar = saludar
        self.hacer_examen = hacer_examen
        self.salir_del_salon = salir_del_salon
        self.__responder_el_examen = responder_el_examen
        self.__entregar_tarea = entregar_tarea
        self.__recibir_las_notas = recibir_las_notas

    def saludo (self):
        print(f"darwin vamos a {self.saludar} al profe")

    def examen (self):
        print(f"berro, darwin vamos a {self.hacer_examen} porque tenemos 5 minutos")

    def salir (self):
        print(f"bueno profe nos vemos, darwin vamos a {self.salir_del_salon}")
        
    def responder (self):
        print(f"listo ya voy a {self.__responder_el_examen}")

    def entregar (self):
        print(f"ya es hora de {self.__entregar_tarea}")

    def recibir (self):

        print(f"ya voy a {self.__recibir_las_notas}\ncomo que saque 01? ")

deivis = Alumno("saludar", "hacer examen", "salir del salon","responder examen", "entrga del examen", "recibir notas")

deivis.saludo()
deivis.examen()
deivis.salir()
deivis.responder()
deivis.entregar()
deivis.recibir()
