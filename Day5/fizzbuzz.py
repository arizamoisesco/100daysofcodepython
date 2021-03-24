#Generamos los 100 números y guardarlos en un array

for numero in range(1, 101):
    
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
#Verificamos si son divisibles por 3, si es el caso lanzar un menzaje que diga "fizz"
#Verificamos si es divisible por 5, si es el caso lanzamos un mensaje que diga "Buzz"
#Verificamos si es divisible por 15, entonces lanzamos el mensaje "Fizzbuzz"