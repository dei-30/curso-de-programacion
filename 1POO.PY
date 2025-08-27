class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        print(f"El libro '{self.titulo}' de {self.autor} tiene {self.num_paginas} páginas.")

    def es_largo_libro(self, umbral_paginas):
        return self.num_paginas > umbral_paginas
    
print("--- Información de 'El principito' ---")
el_principito = Libro("El principito", "Antoine de Saint-Exupéry", 96)
el_principito.mostrar_informacion()
umbral_de_paginas = 200
es_largo = el_principito.es_largo_libro(umbral_de_paginas)
print(f"¿Es un libro largo? {es_largo}")

print("\n""--- Información de 'Don Quijote de la Mancha' ---")
don_quijote = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1072)
don_quijote.mostrar_informacion()
es_largo = don_quijote.es_largo_libro(umbral_de_paginas)
print(f"¿Es un libro largo? {es_largo}")

