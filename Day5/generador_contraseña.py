#Password Generator Project
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
cantidad_letras= int(input("¿Cuántas letras quiere que tenga?\n")) 
cantidad_simbolos = int(input(f"¿Cuántos simbolos le gustaria que tuviera?\n"))
cantidad_numeros = int(input(f"¿Cuántos números le gustaria usar\n"))

#Generar la letra aleatoria con base en el tamaño del grupo de letras

contraseña = ""
#Hacer un ciclo que recorra y con base al número entregado por el usuario 
print("*"*5)
for i in range(0, cantidad_letras):
    letra_aleatoria = random.randint(0, len(letras)-1)
    print(f'Letra aleatorio: {letra_aleatoria}')
    contraseña += letras[letra_aleatoria]

for i in range(1, cantidad_simbolos):
    simbolo_aleatorio =  random.randint(0, len(simbolos)-1) 
    print(f'símbolo aleatorio: {simbolo_aleatorio}') 
    contraseña += simbolos[simbolo_aleatorio]

for i in range(0, cantidad_numeros):
    numero_aleatorio =  random.randint(0, len(numeros)-1)  
    print(f'numero aleatorio: {numero_aleatorio}')
    contraseña += numeros[numero_aleatorio]

print('*'*5)
print(contraseña)
print(letra_aleatoria)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
