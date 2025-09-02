from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, costo_base, numero_puertas):
        self.marca = marca
        self.modelo = modelo
        self.costo_base = costo_base
        self.numero_puertas = numero_puertas

    @abstractmethod
    def calcular_costo_mantenimiento(self):
        pass

    def mostrar_info(self):
        print(f"La marca: {self.marca}\nEl modelo: {self.modelo}\nTiene: {self.numero_puertas} puertas.")
        print(f"Costo de mantenimiento: ${self.calcular_costo_mantenimiento()}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, costo_base, numero_puertas):
        super().__init__(marca, modelo, costo_base, numero_puertas)
        self.numero_puertas = numero_puertas

    def calcular_costo_mantenimiento(self):
        return self.costo_base * self.numero_puertas


class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, costo_base, numero_ruedas):
        super().__init__(marca, modelo, costo_base, numero_ruedas)
        self.numero_ruedas = numero_ruedas

    def calcular_costo_mantenimiento(self):
        return self.costo_base / 2



mi_carro = Automovil("TOYOTA", "COROLLA", 200, 4)
mi_moto = Motocicleta("VERA", "nose", 100, 2)


print("Información del Automovil:")
mi_carro.mostrar_info()
print("\nInformación de la Motocicleta:")
mi_moto.mostrar_info()