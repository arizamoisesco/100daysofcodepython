print("Bienvenido a la calculadora de años bisiestos\n")
año = int(input("Ingrese el año al que desea averiguar si es bisiesto: "))
divisible4 = año % 4
print(divisible4)
divisible100 = año % 100
print(divisible100)
divisible400 = año % 400
print(divisible400)

if divisible4 == 0:
    if divisible100 == 0:
        if divisible400 == 0:
            print("El año es bisiesto")
        else:
            print("Este año no es bisiesto")
    else:
        print("Este año es bisiesto")
else: 
    print("Este año no es bisiesto")
        
