#Alvaro Jose Chancafe Araujo

#----------------------------------------------------Ejercicio 7--------------------------------------------------------#
#Dado el diccionario que almacena la talla de algunas personas {'Marcelo': 1.80, 'José':1.50, 'Oscar':1.70, 'Jorge': 1.40}, 
# escriba un programa que dada una talla por el usuario imprima el nombre.




dict = {"Marcelo": 1.80, 'José': 1.50, 'Oscar': 1.70, 'Jorge': 1.40}

print("Tenemos 4 tallas: 1.80, 1.50, 1.70, 1.40")

talla = input("Elija una talla para saber a que persona le pertence: ")


list_of_key = list(dict.keys())   
list_of_value = list(dict.values()) 

while talla not in("1.80", "1.50", "1.70", "1.40"):
    talla = (input("Seleccione una talla existente: "))

if talla == "1.80": 
    talla = 1.80
    posicion = list_of_value.index(1.80) 
    print(list_of_key[posicion])

if talla == "1.50": 
    talla = 1.50
    posicion = list_of_value.index(1.50)
    print(list_of_key[posicion])

if talla == "1.70": 
    talla = 1.70
    posicion = list_of_value.index(1.70)
    print(list_of_key[posicion])

if talla == "1.40": 
    talla = 1.40
    posicion = list_of_value.index(1.40)
    print(list_of_key[posicion])



   