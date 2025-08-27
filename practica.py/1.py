print("---------------------TE AMOOOO-----------------------")

def corazon():
    mensaje = " TE AMO MI NIÑA ♥ "
    fila_mensaje = 6  

    for y in range(15, -15, -1):
        linea = ""
        for x in range(-30, 30):
            if ((x * 0.04)**2 + (y * 0.09)**2 - 1)**3 - (x * 0.04)**2 * (y * 0.09)**3 <= 0:
                linea += "*"
            else:
                linea += " "
        
        
        if y == fila_mensaje:
            inicio = (len(linea) - len(mensaje)) // 2
            linea = linea[:inicio] + mensaje + linea[inicio + len(mensaje):]
        
        print(linea)

corazon()