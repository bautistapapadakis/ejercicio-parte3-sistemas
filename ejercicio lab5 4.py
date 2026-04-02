contrasena = input("hacete una contrasena:")

longitud = len(contrasena) >= 8
mayuscula = any(c.isupper() for c in contrasena)
minuscula = any(c.islower() for c in contrasena)
numero = any(c.isdigit() for c in contrasena)
especial = any(not c.isalnum() for c in contrasena)

if (longitud and mayuscula and minuscula 
    and numero and especial):
    print("Contrasen válida")
else:
    print("Contrasena no válida")