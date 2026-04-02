
peso = float(input("ingrese su peso:"))
altura = float(input("ingrese su altura:"))

imc = peso / (altura * altura)

print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    print("Talla S")
elif imc < 25:
    print(" Talla M")
elif imc < 30:
    print("Talla L")
else:
    print("Talla XL")