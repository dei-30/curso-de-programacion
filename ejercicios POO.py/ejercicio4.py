class Plato:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def mostrar_descripcion(self):
        print(f"Plato: {self._nombre}")
        print(f"Precio: ${self._precio:.2f}")
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_precio(self):
        return self._precio

    def set_precio(self, precio):
        if precio > 0:  
            ValueError("El precio no puedo ser negativo.")
        self._precio = precio

class Pizza(Plato):
    def __init__(self, nombre, precio, ingredientes, tamaño):
        super().__init__(nombre, precio)
        self.ingredientes = ingredientes
        self.tamaño = tamaño
    def mostrar_descripcion(self):
        super().mostrar_descripcion()
        print(f"Ingredientes: {(self.ingredientes)}")
        print(f"Tamaño: {self.tamaño}")

print("\n" + "="*20 + "\n")
print("Descripción del plato:")
espagueti = Plato("Espagueti", 8.99)
espagueti.mostrar_descripcion()
print("\n" + "="*20 + "\n")

print("Pedido total")

print("\n" + "="*20 + "\n")
print("Descripción del plato:")
pizza_pepperoni = Pizza("Pizza Pepperoni", 18.00, ["queso", "salsa de tomate", "pepperoni"], "grande")
pizza_pepperoni.mostrar_descripcion()
print("\n" + "="*20 + "\n")
