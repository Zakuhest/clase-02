# Ejercicio 3: Dada la matriz, [[1,2,3],[4,5,6],[7,8,9]], calcule el promedio de la diagonal principal.
# Hint: Los 3 elementos de la diagonal son 1,5,9

matriz = [[1,2,3],[4,5,6],[7,8,9]]
suma=0

for x in range (0,3):
    suma += matriz[x][x]
prom=suma/3

print(f"\nLista Actual: {matriz}")
print(f"\nSuma: {suma}")
print(f"Promedio: {prom}")