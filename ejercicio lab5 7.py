


precio = float(input("Ingrese el precio original del artículo: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

monto_descuento = precio * (descuento / 100)


precio_final = precio - monto_descuento

# Mostrar resultado
print("\n💰 Precio original:", precio)
print("📉 Descuento aplicado:", monto_descuento)
print("✅ Precio final:", precio_final)