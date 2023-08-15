# Ejercicio 4b
# Dada una lista de números enteros [15,20,50,80,40,60], escriba un programa que dado un dato por el usuario, este sea eliminado de la lista.
# Tome en cuenta que el usuario ingresará datos que se encuentran dentro de la lista

numeros=[15,20,50,80,40,60]

print(f"\nLista Actual: {numeros}")

num = int(input("\nIngrese el dato a eliminar: "))

numeros.remove(num)

print(f"\nLista Modificada: {numeros}")