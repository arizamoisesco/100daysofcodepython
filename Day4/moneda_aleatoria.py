import random 

moneda = random.randint(0,1)

if moneda == 0:
    print("Head")
elif moneda == 1:
    print("Tail")
else:
    print('Número fuera del rango necesario')