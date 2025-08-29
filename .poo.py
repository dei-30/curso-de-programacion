class Coche:
    def __init__(self, color):
        self.color = color
        self.encendido = False

    def encender(self):
        self.encendido = True

    def acelerar(self):
        if self.encendido:
            print("El coche está acelerando. ¡Vroom!")
        else:
            print("No puedes acelerar. El coche está apagado.")

mi_coche = Coche("rojo")
mi_coche.acelerar()  
mi_coche.encender()
mi_coche.acelerar()  