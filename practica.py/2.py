import random
print("-------------------Adivina el numero-------------------")

numero_loco = random.randint(1, 10)

for intento in range(1, 4):
    entrada = input("Ingresa un número entre 1 y 10: ")

    if not entrada.isdigit():
        print("😡 ¡Eso no es un número, mi pana! No me vengas con letras, escribe un número del 1 al 10.")
        continue

    numero = int(entrada)

    if numero < 1 or numero > 10:
        print("Te saliste del rango cabezón, es un número del 1 al 10 ¿por qué pones otro?")
        continue

    if numero == numero_loco:
        print("🎉 ¡CORRECTO ESE MERO ERAAA! Ganaste, eres un crack 😎")
        break
    else:
        if intento < 3:
            print(f"❌ Ño, dale otra vez... llevas {intento} intento(s).")
        else:
            print(f"💀 NOOO PERDISTEEE BOBOOO. El número correcto era {numero_loco}")