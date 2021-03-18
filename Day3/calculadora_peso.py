print("Bienvenido a la calculadora de peso, vamos a ver si estas en tu peso ideal\n")
print("Ingresa los siguientes datos solicitados:\n")
peso = float(input("ingrese su peso actual: "))
altura = float(input("Ingrese su altura actual: "))

imc = round(peso / (altura **2))

if imc <= 18.5:
    print(f"Cuidado tu {imc} representa que tienes bajo peso")
elif imc > 18.5 and imc < 25:
    print("Su peso es normal")
elif imc > 25 and imc < 30:
    print("Ojo esta en sobrepeso")
elif imc > 30 and imc < 35:
    print("Cuidado ya esta obeso")
else:
    print("Estas en un peso riesgoso para tu salud")

