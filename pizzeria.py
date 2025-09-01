class Ingredientes:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pizza:
    def __init__(self, nombre, tamaño, precio):
        self.nombre = nombre
        self.tamaño = tamaño
        self.precio = precio
        self.ingredientes = []

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def mostrar_detalles(self):
        print(f"------DETALLES DE LA PIZZA------")
        print(f"Pizza: {self.nombre}, Tamaño: {self.tamaño}")
        print("Ingredientes:")
        for ingrediente in self.ingredientes:
            print(f"- {ingrediente.nombre} (${ingrediente.precio})")
        total = self.precio + sum(ingrediente.precio for ingrediente in self.ingredientes)
        print(f"Precio base: ${self.precio}")
        print(f"Total de la pizza: ${total}")
        print("-" * 30)

class Pedido:
    def __init__(self):
        self.pizzas = []

    def acciones (self, numero_pedido, agregar_pizza, calcular_total_pedido, mostrar_detalles_pedido):
        self.numero_pedido = numero_pedido
        self.agregar_pizza = agregar_pizza
        self.calcular_total_pedido = calcular_total_pedido
        self.mostrar_detalles_pedido = mostrar_detalles_pedido

    def agregar_pizza(self, pizza):
        self.pizzas.append(pizza)
        print(f"Se ha agregado una pizza con los detalles que tu escogistes.")
    

    def calcular_total_pedido(self):
        precio_pizza = super().calcular_total_pedido()
        return precio_pizza + sum(ingrediente.precio for ingrediente in super().ingredientes)


    def mostrar_detalles_pedido(self):
        print("------DETALLES DEL PEDIDO------")
        for pizza in self.pizzas:
            pizza.mostrar_detalles()
        print(f"Total del pedido: {self.calcular_total_pedido()}")
        print("-" * 30)

lista_ingredientes = [
    Ingredientes("Peperoni " , 1.00),
    Ingredientes("champiñones", 1.50),
    Ingredientes("doble queso", 3.00),
    Ingredientes("maiz", 2.00)
]  

lista_pizzas = [
    Pizza ("pizza mediana de peperoni con maiz", "mediana", 8.00),
    Pizza ("pizza pequeña con doble queso", "pequeña", 6.00),
    Pizza ("pizza con champiñones", "grande", 10.00)
]

pizza_personalizada = Pizza("El especial", "mediana", 8.00)


pizza_personalizada.agregar_ingrediente(lista_ingredientes[0])  
pizza_personalizada.agregar_ingrediente(lista_ingredientes[2])  
pizza_personalizada.agregar_ingrediente(lista_ingredientes[3])  


pizza_personalizada.mostrar_detalles()