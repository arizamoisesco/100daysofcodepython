#Generar los números de 1 a 100 
total_numeros_pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        total_numeros_pares += numero

total = total_numeros_pares + 1
print(f"El total de la suma de números pares + 1 es: {total}")
#Crear un condicional y si los números son pares se suma 
#Sumarle 101 que seria el valor de la suma 1 + 100 que hay que tener en cuenta en el resultado
