def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
monto1 = 200
monto2 = 150

# Llamada con porcentaje por defecto (10%)
descuento1 = calcular_descuento(monto1)
print(f"Monto total: ${monto1}")
print(f"Descuento aplicado (10%): ${descuento1}")
print(f"Monto final a pagar: ${monto1 - descuento1}\n")

# Llamada con porcentaje personalizado (por ejemplo, 15%)
descuento2 = calcular_descuento(monto2, 15)
print(f"Monto total: ${monto2}")
print(f"Descuento aplicado (15%): ${descuento2}")
print(f"Monto final a pagar: ${monto2 - descuento2}")
