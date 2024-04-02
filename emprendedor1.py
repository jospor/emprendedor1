import math

suscripcion = float(input("Ingrese el precio de suscripcion: \n"))
usuarios = float(input("Ingrese el numero de usuarios: \n"))
total = float(input("Ingrese el gasto total: \n"))

Utilidades = (suscripcion * usuarios) - total

print(f"Las utilidades son: ${Utilidades}")
