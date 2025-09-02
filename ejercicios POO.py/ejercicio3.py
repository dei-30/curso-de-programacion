class Animal:
    def __init__(self, nombre, edad ):
        self.__nombre = nombre
        self.__edad = edad
        
    def get_nombre (self):
        return self.__nombre
    def set_edad (self):
        return self.__edad
    def hacer_sonido(self):
        return "Sonido generico"

class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza
    def hacer_sonido(self):
        return "Guau Guau"

class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color
    def hacer_sonido(self):
        return "Miau Miau"

mi_perro = Perro("Toby", 5, "Pastor Aleman")
print(f"Mi perro se llama {mi_perro.get_nombre()} y tiene {mi_perro.set_edad()} años, y su raza es de un {mi_perro.raza}")
print(f"Y tambien hace un sonido: {mi_perro.hacer_sonido()}")

print("-" * 30)

mi_gato = Gato("Garfield", 3, "Naranja")
print(f"Mi gato se llama {mi_gato.get_nombre()} y tiene {mi_gato.set_edad()} años, y es de color {mi_gato.color}")
print(f"Y tambien hace un sonido: {mi_gato.hacer_sonido()}")