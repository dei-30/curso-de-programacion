import random

def jugar():
    """Función principal del juego de piedra, papel o tijera."""
    lista = ["piedra", "papel", "tijera"]
    
    print("---------Hablame menol, llegate vamo a jugar fuegooo----------")
    
    while True:
        jugador = input("Elige piedra, papel o tijera:\n(o sino te da la fokin gana de jugar pone 'ño bb' y te sales de esta monda): ").lower()
        
        if jugador == "ño bb":
            print("Nos pillamnos bro, te me cuidas el dulce.")
            break
        
        if jugador not in lista:
            print("Mira cabeza de ñame que no sabes jugar?, elige entre piedra, papel o tijera.")
            continue
        
        computadora = random.choice(lista)
        print(f"La computadora eligió: {computadora}")
        
        if jugador == computadora:
            print("Empate cachon 🤝")
            print("Pero pa mis cjn dale otra vez porque empatados no vamos a quedar")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print("GANASTE UN DUROO BROOO 💪\nYo te mamo la bola derecha sin tocarte la izquierda\notra khe?")
        else:
            print("Perdiste 😩\npor gay JAJAJJAJJAJA BOBOOOO\nQuedaste picao velda? dale otra vez")
            
jugar()
