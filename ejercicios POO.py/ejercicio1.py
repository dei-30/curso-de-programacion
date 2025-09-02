
from abc import ABC, abstractmethod


def registrar_calculo(cls):
    def operacion(self, *args, **kwargs):
        resultado = cls(self, *args, **kwargs)
        print(f"Se ha calculado el {cls.__name__.replace('calcular_', '')} de un {self.__class__.__name__}. El resultado es: {resultado:.2f}")
        return resultado
    return operacion

class FiguraGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, valor):
        if valor <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self._radio = valor

    @registrar_calculo
    def calcular_area(self):
        return 3.14159 * (self.radio ** 2)

    @registrar_calculo
    def calcular_perimetro(self):
        return 2 * 3.14159 * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, ancho, alto):
        self._ancho = ancho
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor <= 0:
            ValueError("El ancho debe ser un número positivo.")
        self._ancho = valor

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor <= 0:
             ValueError("El alto debe ser un número positivo.")
        self._alto = valor

    @registrar_calculo
    def calcular_area(self):
        return self.ancho * self.alto

    @registrar_calculo
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.alto)


print("-" * 30)
mi_circulo = Circulo(5)
mi_circulo.calcular_area()
mi_circulo.calcular_perimetro()

print("-" * 30)

mi_rectangulo = Rectangulo(4, 6)
mi_rectangulo.calcular_area()
mi_rectangulo.calcular_perimetro()
print("-" * 30)