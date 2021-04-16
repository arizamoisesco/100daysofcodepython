def prime_checker(number):
    contador = 0
    
    for n in range(1,number+1):
        modulo = number % n
        if (modulo == 0):
            contador += 1

    if contador == 2:
        print("El número es primo")
    else:
        print("El número no es primo")
        

n = int(input("Check this number: "))
prime_checker(number=n)