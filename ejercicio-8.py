"""
Ejercicio 8
Guarde los datos de una persona (nombre,apellido,edad) en un diccionario, luego imprimalo en el siguiente formato. "Hola mi nombre es [nombre] [apellido], y tengo [edad] años.
"""

name = input("Escribe tu nombre: ")

last_name = input("Escribe tu apellido: ")

age = int(input("Escribe tu edad: "))

datos = {
    'nom' : name,
    'ap' : last_name,
    'ed' : age
}

print(f"Hola mi nombre es {datos.get('nom')} {datos.get('ap')} y tengo, {datos.get('ed')} años.")
