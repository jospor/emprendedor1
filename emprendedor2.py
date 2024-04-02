
def calcular_utilidades(precio_suscripcion, usuarios_normales, usuarios_premium, gastos_totales):
    ingresos_normales = precio_suscripcion * usuarios_normales
    ingresos_premium = precio_suscripcion * 1.5 * usuarios_premium
    ingresos_totales = ingresos_normales + ingresos_premium
    utilidades = ingresos_totales - gastos_totales
    return utilidades

precio_suscripcion = float(input("Ingrese el precio de suscripción (P): "))
usuarios_normales = int(input("Ingrese el número de usuarios normales (Unormal): "))
usuarios_premium = int(input("Ingrese el número de usuarios premium (Upremium): "))
gastos_totales = float(input("Ingrese el gasto total (GT): "))

utilidades = calcular_utilidades(precio_suscripcion, usuarios_normales, usuarios_premium, gastos_totales)

print(f"Las utilidades son: ${utilidades}")
