import random
import string


longitud = int(input("Ingrese la longitud de la contraseña: "))


letras = string.ascii_letters      
numeros = string.digits           
especiales = string.punctuation   


todos = letras + numeros + especiales


password = ""
for i in range(longitud):
    password += random.choice(todos)


print("\n🔐 Contraseña generada:")
print(password)