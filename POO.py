class personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        print(f"Nombre: {self.nombre}\nFuerza: {self.fuerza}\nInteligencia: {self.inteligencia}\nDefensa: {self.defensa}\nVida: {self.vida}")

    def subir_nivel(self, fuerza, inteligencia, defensa, vida):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"{self.nombre} ha muerto")

    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa)

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")
        if enemigo.esta_vivo():
            print(f"La vida de {enemigo.nombre} es {enemigo.vida}")
        else:
            enemigo.morir()

class guerrero(personaje):
    # La espada ahora tiene un valor fijo de 10
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = 10

    def daño(self, enemigo):
        return max(0, self.fuerza * self.espada - enemigo.defensa)

class mago(personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def atributos(self):
        super().atributos()
        print(f"Libro: {self.libro}")

    def daño(self, enemigo):
        return max(0, self.inteligencia * self.libro - enemigo.defensa)


# Creamos las instancias de las clases
mi_personaje = personaje("el_mata_gays", 20, 15, 10, 100)
# Ya no necesitamos pasar el argumento de la espada
mi_guerrero = guerrero("Goku", 15, 10, 8, 100)
mi_mago = mago("Maguito", 10, 20, 5, 100, 12)

# Ahora, el guerrero tendrá la espada con daño 10 por defecto
print("--- Atributos de Guerrero ---")
mi_personaje.atributos()
print("\n--- Atributos de Guerrero ---")
mi_guerrero.atributos()
print(f"Espada: {mi_guerrero.espada}")
print("\n--- Atributos de Mago ---")
mi_mago.atributos()

print("\n----EMPIENZA EL COMBATE----\n")

goku = guerrero("Goku", 15, 10, 8, 100)
maguito = mago("Maguito", 10, 20, 5, 100, 12)
el_mata_gays = personaje("el_mata_gays", 20, 15, 10, 100)
el_mata_gays.atacar(maguito)
goku.atacar(el_mata_gays)
maguito.atacar(goku)
goku.atributos()
maguito.atributos()
el_mata_gays.atributos()

print("\n----FIN DEL COMBATE----")
print("----HA GANADO EL MAGO----\n")
