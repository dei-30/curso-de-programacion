class TiendaRopa():
    def __init__(self, nombre,color, precio, sku):
        self.nombre = nombre
        self.color = color
        self.precio = precio
        self.__sku = sku
    
    def mostrar_informacion(self):
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio:.2f}")
        print(f"SKU: {self.__sku}")

    def get_sku (self):
        return self.__sku

class Electronico(TiendaRopa):
    def __init__(self, nombre, color, precio, sku, marca):
        super().__init__(nombre, color, precio, sku)
        self.marca = marca
        self.color = color
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Marca: {self.marca}")
        print(f"Color: {self.color}")

class Ropa(TiendaRopa):
    def __init__(self, nombre, color, precio, sku, talla):
        super().__init__(nombre, color, precio, sku)
        self.talla = talla
        self.color = color

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")

print("\n" + "="*30 + "\n")
laptop = Electronico("Laptop Ultra", "Negro", 1500.00, "EL-LAP-001", "TechCo")
print("Información del Producto Electrónico:")
laptop.mostrar_informacion()

print("\n" + "="*30 + "\n")

camiseta = Ropa("Camiseta de algodón", "Blanco", 25.50, "RO-CAM-012", "L")
print("Información del Producto de Ropa:")
camiseta.mostrar_informacion()
print("\n" + "="*30 + "\n")