#Alvaro Jose Chancafe Araujo
#----------------------------------------------------Ejercicio 6--------------------------------------------------------#
#Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}
# , escriba un programa que dado un nombre ingresado por el usuario imprime la talla.


dict = {"Marcelo": 1.80, 'Jose':1.50, 'Oscar':1.70, 'Jorge': 1.40}

print("Tenemos 4 personas: Marcelo, Jose, Oscar, Jorge")
nombre = input("Elija un nombre para saber su talla: ").capitalize()

while nombre not in list(dict.keys()): 
    nombre = input("Tiene que colocar una opcion valida: ").capitalize()

x = dict.get(nombre)
print(x)

