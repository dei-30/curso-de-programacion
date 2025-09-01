class Alumno:
    def __init__ (self, saludar, hacer_examen, salir_del_salon):
        self.saludar = saludar
        self.hacer_examen = hacer_examen
        self.salir_del_salon = salir_del_salon

    def saludo (self):
        print(f"darwin vamos a {self.saludar} al profe")

    def examen (self):
        print(f"berro, darwin vamos a {self.hacer_examen} porque tenemos 5 minutos")

    def salir (self):
        print(f"bueno profe nos vemos, darwin vamos a {self.salir_del_salon}")
deivis = Alumno("saludar", "hacer examen", "salir del salon")
deivis.saludo()
deivis.examen()
deivis.salir()