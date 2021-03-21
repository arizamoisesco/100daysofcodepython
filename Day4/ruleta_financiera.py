import random

cadena_nombres = input("Ingrese la lista de personas con las que desea apostar separados por comas (,): ")
nombres = cadena_nombres.split(", ")
#Determinar el tamaño de la lista
tamaño_lista = len(nombres)
#Sacar el nombre del ganador con base en la lista de forma aleatoria
numero_ganador = random.randint(0,tamaño_lista -1)

for i in nombres:
    print(i)

print(numero_ganador)
print(nombres[numero_ganador])