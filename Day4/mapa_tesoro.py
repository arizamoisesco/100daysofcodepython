# 🚨 Don't change the code below 👇
fila1 = ["⬜️","⬜️","⬜️"]
fila2 = ["⬜️","⬜️","⬜️"]
fila3 = ["⬜️","⬜️","⬜️"]
mapa = [fila1, fila2, fila3]
print(f"{fila1}\n{fila2}\n{fila3}")
posicion = input("¿Dónde quieres poner el tesoro? ")
# 🚨 Don't change the code above 👆
columna_escogida = int(posicion[0]) 
fila_escogida = int(posicion[1])
#Write your code below this row 👇
mapa[fila_escogida - 1][columna_escogida -1] = "🪙"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{fila1}\n{fila2}\n{fila3}")