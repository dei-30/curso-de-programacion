import time

class Guerrero:
    def __init__(self, nombre, vida, ataque, defensa, tipo):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.tipo = tipo

    def atacar(self, objetivo):
        daño = max(0, self.ataque - objetivo.defensa)  # Evitar daño negativo
        objetivo.vida -= daño
        print(f"{self.nombre} ha realizado {daño} puntos de daño a {objetivo.nombre}")

    def curarse(self):
        botiquin = 30
        self.vida += botiquin
        print(f"{self.nombre} se ha curado 30 puntos de vida. Vida actual: {self.vida}")

    def mostrar_estado(self):
        print(f"Guerrero: {self.nombre}, Vida: {self.vida}, Ataque: {self.ataque}, Defensa: {self.defensa}, Tipo: {self.tipo}")


class Clan:
    def __init__(self, nombre, lista_guerreros, estrategia):
        self.nombre = nombre
        self.lista_guerreros = lista_guerreros
        self.estrategia = estrategia

    def agregar_guerrero(self, guerrero):
        self.lista_guerreros.append(guerrero)
        print(f"Guerrero {guerrero.nombre} agregado al clan {self.nombre}")

    def seleccionar_guerrero(self, nombre):
        for guerrero in self.lista_guerreros:
            if guerrero.nombre == nombre:
                return guerrero
        print(f"Guerrero {nombre} no encontrado en el clan {self.nombre}")
        return None

    def atacar_clan(self, objetivo_clan):
        print(f"El clan {self.nombre} ataca al clan {objetivo_clan.nombre}")
        for guerrero in self.lista_guerreros:
            if objetivo_clan.lista_guerreros:
                objetivo = objetivo_clan.lista_guerreros[0]
                guerrero.atacar(objetivo)
                if objetivo.vida <= 0:
                    print(f"{objetivo.nombre} ha sido derrotado")
                    objetivo_clan.lista_guerreros.remove(objetivo)

    def estado_clan(self):
        print(f"Estado del clan {self.nombre}:")
        for guerrero in self.lista_guerreros:
            guerrero.mostrar_estado()


class Batalla:
    def __init__(self, clan1, clan2):
        self.clan1 = clan1
        self.clan2 = clan2

    def iniciar(self):
        print("¡La batalla ha comenzado!")
        while self.clan1.lista_guerreros and self.clan2.lista_guerreros:
            self.clan1.atacar_clan(self.clan2)
            if not self.clan2.lista_guerreros:
                print(f"El clan {self.clan1.nombre} ha ganado la batalla")
                break
            self.clan2.atacar_clan(self.clan1)
            if not self.clan1.lista_guerreros:
                print(f"El clan {self.clan2.nombre} ha ganado la batalla")
                break

    def verificar_ganador(self):
        if not self.clan1.lista_guerreros:
            return self.clan2.nombre
        elif not self.clan2.lista_guerreros:
            return self.clan1.nombre
        return None


# Crear guerreros
guerrero1 = Guerrero("Darwin", 100, 30, 20, "Espadachín")
guerrero2 = Guerrero("Dickson", 80, 25, 15, "Arquero")
guerrero3 = Guerrero("Julio", 120, 35, 25, "Arquero")
guerrero4 = Guerrero("Elio", 90, 20, 10, "Mago")

# Crear clanes
clan1 = Clan("Clan A", [guerrero1, guerrero2], "Ofensiva")
clan2 = Clan("Clan B", [guerrero3, guerrero4], "Defensiva")

# Bucle para repetir la batalla hasta que uno de los clanes gane
while clan1.lista_guerreros and clan2.lista_guerreros:
    # Mostrar estado inicial
    print("\n========================================")
    print("Estado inicial de los clanes:")
    print("========================================\n")
    clan1.estado_clan()
    print()  # Salto de línea
    clan2.estado_clan()
    print("\n========================================")

    # Iniciar batalla
    print("\n¡Iniciando batalla!\n")
    batalla = Batalla(clan1, clan2)
    batalla.iniciar()

    # Mostrar estado después de la batalla
    print("\n========================================")
    print("Estado después de la batalla:")
    print("========================================\n")
    clan1.estado_clan()
    print()  # Salto de línea
    clan2.estado_clan()
    print("\n========================================")

# Determinar el ganador
print("\n========================================")
if not clan1.lista_guerreros:
    print(f"\nEl clan {clan2.nombre} ha ganado la guerra definitiva.")
elif not clan2.lista_guerreros:
    print(f"\nEl clan {clan1.nombre} ha ganado la guerra definitiva.")
print("========================================\n")

time.sleep(3)