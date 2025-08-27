class Producto:
    def __init__(self, nombre, precio, cantidad_disponible):
        self.nombre = nombre
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

    def vender(self, cantidad):
        if cantidad <= self.cantidad_disponible:
            self.cantidad_disponible -= cantidad
            costo_total = self.precio * cantidad
            print(f"Venta exitosa de {cantidad} unidades de {self.nombre}.")
            return costo_total
        else:
            print(f"No hay suficientes unidades de {self.nombre} para esta venta. Solo quedan {self.cantidad_disponible}.")
            return 0

class Tienda:  
    def __init__(self):
        self.inventario = {}  

    def agregar_producto(self, producto):
        self.inventario[producto.nombre] = producto
        print(f"Producto '{producto.nombre}' agregado con éxito.")

    def realizar_venta(self, nombre_producto, cantidad):
        if nombre_producto in self.inventario:
            producto = self.inventario[nombre_producto]
            costo_total = producto.vender(cantidad)
            if costo_total > 0:
                print(f"Costo total de la venta: ${costo_total:.2f}")
        else:
            print(f"Producto '{nombre_producto}' no encontrado en el inventario.")

    def mostrar_inventario(self): 
        print("\n------ Inventario de la tienda ----------")
        if not self.inventario:
            print("El inventario está vacío.")
        else:
            for nombre, producto in self.inventario.items():
                print(f"Producto: {producto.nombre}, Precio: ${producto.precio}, Cantidad disponible: {producto.cantidad_disponible}")

        print("------------------------------------")


mi_tienda = Tienda()
leche = Producto("leche", 1.50, 10)
pan = Producto("pan", 2.25, 50)
huevos = Producto("huevos", 1.00, 20)

mi_tienda.agregar_producto(leche)
mi_tienda.agregar_producto(pan)
mi_tienda.agregar_producto(huevos)

mi_tienda.mostrar_inventario()

mi_tienda.realizar_venta("leche", 2)
mi_tienda.realizar_venta("pan", 20)
mi_tienda.realizar_venta("huevos", 40)  # Venta fallida
mi_tienda.realizar_venta("jugo", 1)  # Venta de producto inexistente

mi_tienda.mostrar_inventario()