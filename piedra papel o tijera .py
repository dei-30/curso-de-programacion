import random

def jugar():
    """Función principal del juego de piedra, papel o tijera."""
    lista = ["piedra", "papel", "tijera"]
    
    print("---------Hablame menol, llegate vamo a jugar fuegooo----------")
    
    while True:
        jugador = input("Elige piedra, papel o tijera (o sino te da la fokin gana de jugar pone 'ño bb' y te sales de esta monda): ").lower()
        
        if jugador == "ño bb":
            print("Nos pillamnos bro, te me cuidas el dulce.")
            break
        
        if jugador not in lista:
            print("Mira cabeza de ñame que no sabes jugar?, elige entre piedra, papel o tijera.")
            continue
        
        computadora = random.choice(lista)
        print(f"La computadora eligió: {computadora}")
        
        if jugador == computadora:
            print("¡Empate bro! 🤝")
            print("Pero pa mis cjn dale otra vez porq empatado no vamos a quedar")
        elif (jugador == "piedra" and computadora == "tijera") or \
             (jugador == "papel" and computadora == "piedra") or \
             (jugador == "tijera" and computadora == "papel"):
            print(" UN DUROO BROOO 💪")
        else:
            print("¡Perdiste! por gay")
        
        print("Dale otra fuego? (quede picado)")
jugar()