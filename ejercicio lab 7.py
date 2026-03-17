nombre = input('ingrese nombre:')
edad = int(input("Ingrese edad: "))
ciudad= input('ingrese ciudad:')

año_actual = 2026
año_nacimiento = año_actual - edad


print("Nombre:", nombre)
print("Edad:", edad)
print("Ciudad:", ciudad)
print("Año de nacimiento:", año_nacimiento)

if edad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

# Verificar si la edad es múltiplo de 5
if edad % 5 == 0:
    print("Tu edad es múltiplo de 5")
else:
    print("Tu edad NO es múltiplo de 5")