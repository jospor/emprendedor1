
def calcular_utilidades(precio_suscripcion, numero_usuarios, gastos_totales):
    ingresos = precio_suscripcion * numero_usuarios
    utilidades = ingresos - gastos_totales
    return utilidades

precio_suscripcion = float(input("Ingrese el precio de suscripción (P): "))
numero_usuarios = int(input("Ingrese el número de usuarios (U): "))
gastos_totales = float(input("Ingrese el gasto total (GT): "))
utilidades_anterior = float(input("Ingrese las utilidades del año anterior (Uanterior): "))

utilidades_actuales = calcular_utilidades(precio_suscripcion, numero_usuarios, gastos_totales)

razon_utilidades = utilidades_actuales / utilidades_anterior if utilidades_anterior != 0 else float('inf')

print(f"Las utilidades actuales son: ${utilidades_actuales}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")

