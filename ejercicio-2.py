"""
Ejercicio 2: Haga un programa en Python que le pida al usuario tantos enteros como quiera, luego cree dos listas, 
una con la lista de números propuestos y la otra con
el número de ocurrencias. Por ejemplo, si el usuario ingresa 4,4,8,4,9,7,7, la primera lista
debe ser [4,8,9,7] y el segundo [3,1,1,2] 
"""
datos = []

veces = int(input("¿Cuantas veces deseas ingresar los datos enteros?\n "))
for i in range(veces):
  dato = int(input("Ingrese un número entero a la lista: "))
  datos.append(dato)

print(f"Lista inicial: {datos}")

sin_repeticion = []
for item in datos:
    if item not in sin_repeticion:
        sin_repeticion.append(item)

print(f"\nLa lista sin repeticiones es: {sin_repeticion}")

cantidad = []
for j in sin_repeticion:
  m = datos.count(j)
  cantidad.append(m)

print(f"\nLa lista donde muestra el número de ocurrencia: {cantidad}")
