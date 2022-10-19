"""Ejercicio 4: Dada la siguiente lista ["Hola", "Amigos", "Hoy", True] , escriba un programa que pida al usuario una palabra, dicha palabra debe ser agregada al final y al inicio de la lista.
"""

lista = ["Hola", "Amigos", "Hoy", True]

palabra = input("Escribir una palabra: ")

lista.append(palabra)
lista.insert(0, palabra)

print(lista)