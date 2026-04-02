numero = int(input("ingrese numero entreo positivo:"))

if numero <= 0:
    print("Debe ingresar un número positivo")
else:
    a = 0
    b = 1

    print("Secuencia Fibonacci:")

    for i in range(numero):
        print(a, end=" ")
        a, b = b, a + b