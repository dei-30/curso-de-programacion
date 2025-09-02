from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, mana=100):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.__vida = vida
        self.__mana = mana

    @property
    def mana(self):
        return self.__mana

    @mana.setter
    def mana(self, valor):
        if valor < 0:
            self.__mana = 0
        else:
            self.__mana = valor

    @property
    def vida(self):
        return self.__vida

    @vida.setter
    def vida(self, valor):
        if valor < 0:
            self.__vida = 0
        else:
            self.__vida = valor

    def atributos(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nInteligencia: {self.inteligencia}\nDefensa: {self.defensa}\nVida: {self.vida}")
        

    def esta_vivo(self):
        return self.__vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    @abstractmethod
    def daño(self, enemigo):
        pass
    
    @abstractmethod
    def atacar(self, enemigo):
        pass
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, martillo, mana=100):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, mana)
        self.martillo = martillo
    def atributos(self):
        super().atributos()
        print(f"Martillo: {self.martillo}")

    def atacar(self, enemigo):
        if enemigo.esta_vivo():
            daño = self.daño(enemigo)
            enemigo.vida -= daño
            print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
            if enemigo.esta_vivo():
                print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
            else:
                enemigo.morir()


    def daño(self, enemigo):
        return max(0, self.fuerza * self.martillo - enemigo.defensa)
    

class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, varita, mana=100):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida, mana)
        self.varita = varita
    def atributos(self):
        super().atributos()
        print(f"Varita: {self.varita}")

    def atacar(self, enemigo):
        if enemigo.esta_vivo():
            daño = self.daño(enemigo)
            enemigo.vida -= daño
            print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
            if enemigo.esta_vivo():
                print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
            else:
                enemigo.morir()
            

    def daño(self, enemigo):
        return max(0, self.inteligencia * self.varita - enemigo.defensa)


def batalla(p1, p2):
    turno = 1
    while p1.esta_vivo() and p2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        p1.atacar(p2)
        if not p2.esta_vivo():
            break
        
        p2.atacar(p1)
        if not p1.esta_vivo():
            break
        
        turno += 1

# Creación de personajes
mi_guerrero = Guerrero("Thor", 20, 15, 10, 1000, 30, 100)
mi_mago = Mago("Gandalf", 10, 30, 5, 1000, 25, 100)

print("-" * 30)
mi_guerrero.atributos()
print("-" * 30)
mi_mago.atributos()
print("-" * 30)

print("\n¡La batalla comienza!\n")
batalla(mi_guerrero, mi_mago)

print("\n¡La batalla ha terminado!")
print("-" * 30)
print("El ganador es:", mi_guerrero.nombre)
print("-" * 30)