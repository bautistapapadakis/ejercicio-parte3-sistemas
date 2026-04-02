import random

numero_secreto = random.randint(1, 100)

historial = []

print("Adivina el número (entre 1 y 100)")

while True:
    numero_usuario = int(input("Ingresa un número: "))
    
    historial.append(numero_usuario)
    print("Intento número:", numero_usuario)

    if numero_usuario == numero_secreto:
        print("Adivinaste el número 🎉")
        break
    elif numero_usuario < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")

print("Historial de intentos:", historial)