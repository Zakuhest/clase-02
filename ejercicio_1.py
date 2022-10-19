"""
Ejercicio 1: Hacer un programa que pida al usuario 5 nombres. Crear una lista con los 5 nombres. 
Despues hacer que muestre una frase los pronombres que empiezan con la letra A
"""
nombres = []
frase = []
for i in range(5):
  nombre = input(f"Ingrese el nombre N°{i+1}: ").lower()
  nombres.append(nombre)

print(nombres)

for k in nombres:
  if k[0] == 'a':
    frase.append(k)

print(frase)
